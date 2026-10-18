from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer, DataCollatorForLanguageModeling
from datasets import Dataset
import lml_config
import torch

class LMLCore:
    def __init__(self, model_path):
        self.path = model_path
        self.device = lml_config.DEVICE
        self.model = None
        self.tokenizer = None

    def load_model(self):
        # Load Factory LLM tokenizer and base model
        print(f"Loading Factory LLM to {self.device}: {self.path}")
        self.tokenizer = AutoTokenizer.from_pretrained(self.path)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(
            self.path,
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device == "cuda" else None
        )

    def generate(self, prompt, system_prompt="", max_len=100):
        # Perform single inference for code/structure generation draft
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=max_len)
        return self.tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)

    def build_new_model(self, raw_data, save_dir, persona=""):
        # Convert raw dataset into Hugging Face Dataset format
        instructions = [x.get("instruction", "") for x in raw_data]
        outputs = [x.get("output", "") for x in raw_data]

        raw_dict = {"instruction": instructions, "output": outputs}
        hf_dataset = Dataset.from_dict(raw_dict)

        def preprocess(examples):
            # Tokenize input data (Instruction-Response pairing format)
            texts = [f"### Instruction:\n{i}\n\n### Response:\n{o}" for i, o in zip(examples["instruction"], examples["output"])]
            tokens = self.tokenizer(texts, truncation=True, max_length=lml_config.MAX_LENGTH, padding="max_length")
            tokens["labels"] = tokens["input_ids"].copy()
            return tokens

        print("Executing dataset tokenization pipeline...")
        tokenized_ds = hf_dataset.map(preprocess, batched=True, remove_columns=hf_dataset.column_names)

        # Configure training arguments (Alpha stage placeholder loop)
        args = TrainingArguments(
            output_dir=save_dir,
            per_device_train_batch_size=2,
            gradient_accumulation_steps=4,
            learning_rate=2e-5,
            logging_steps=5,
            save_strategy="epoch",
            fp16=(self.device == "cuda"),
            num_train_epochs=3,
            report_to="none"
        )

        trainer = Trainer(
            model=self.model,
            args=args,
            train_dataset=tokenized_ds,
            data_collator=DataCollatorForLanguageModeling(tokenizer=self.tokenizer, mlm=False),
        )

        print("Starting data injection and model build process (Alpha Placeholder)...")
        trainer.train()

        # Save generated model and tokenizer weights
        trainer.save_model(save_dir)
        self.tokenizer.save_pretrained(save_dir)
        print(f"Model build complete. Saved to: {save_dir}")
