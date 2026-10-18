import sys
import argparse
import os
import math
from lml_core import LMLCore
from lml_dataset_loader import DatasetLoader
from lml_utils import Logger

def analyze_and_recommend_parameters(dataset_path, ftllm_path):
    """
    Analyzes the dataset volume and base model (ftllm) to recommend 
    an optimal parameter size (in Billions) for the new model.
    """
    print("[i] Running pre-flight resource analysis for LML...")

    # 1. Dataset volume analysis (Estimate token count based on file size)
    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset path not found: {dataset_path}")
    
    file_size_bytes = os.path.getsize(dataset_path)
    file_size_mb = file_size_bytes / (1024 * 1024)
    
    # Rough estimation: 1MB of text jsonl is roughly ~250,000 tokens
    estimated_tokens = file_size_mb * 250000
    token_billions = estimated_tokens / 1_000_000_000

    # 2. Base model (ftllm) capacity analysis
    base_model_size_b = 7.0
    if "1b" in ftllm_path.lower():
        base_model_size_b = 1.0
    elif "3b" in ftllm_path.lower():
        base_model_size_b = 3.0
    elif "7b" in ftllm_path.lower():
        base_model_size_b = 7.0
    elif "13b" in ftllm_path.lower():
        base_model_size_b = 13.0
    elif "70b" in ftllm_path.lower():
        base_model_size_b = 70.0

    # 3. Recommendation logic
    recommended_min_b = max(0.5, round(token_billions / 20, 1))
    recommended_max_b = min(base_model_size_b, round(token_billions / 5, 1))

    if recommended_min_b > recommended_max_b:
        recommended_max_b = recommended_min_b + 1.0

    print("\n" + "="*45)
    print(" 🚀 LML PRE-FLIGHT RESOURCE ANALYSIS")
    print("="*45)
    print(f" - Dataset Size     : {file_size_mb:.2f} MB (~{token_billions:.3f}B tokens est.)")
    print(f" - Base Engine      : {ftllm_path} (~{base_model_size_b}B capacity)")
    print(f" - Recommended Size : {recommended_min_b}B ~ {recommended_max_b}B")
    print("="*45 + "\n")

    # Prompt user for target parameter size input
    try:
        user_input = input(f"Enter target parameter size in Billions [Default {recommended_min_b}B]: ").strip()
        if user_input == "":
            selected_b = recommended_min_b
        else:
            selected_b = float(user_input)
    except ValueError:
        selected_b = recommended_min_b
        print(f"[!] Invalid input. Defaulting to {selected_b}B.")

    print(f"[i] Target model parameter size set to: {selected_b}B\n")
    return selected_b

class LMLEngine:
    def __init__(self, dataset_path, ftllm_path, output_path="output.jsonl", enable_logging=False, log_dir="."):
        self.dataset_path = dataset_path
        self.ftllm_path = ftllm_path
        self.output_path = output_path
        self.enable_logging = enable_logging
        self.log_dir = log_dir

        if self.enable_logging:
            Logger.log(f"Initialization started. Dataset path: {self.dataset_path}", log_dir=self.log_dir)

        # Load meta-AI developer persona markdown file safely for Ubuntu/Linux
        if getattr(sys, 'frozen', False):
            base_path = os.path.dirname(sys.executable)
        else:
            base_path = os.path.dirname(os.path.abspath(__file__))

        persona_path = os.path.join(base_path, "lml_persona.md")

        if not os.path.exists(persona_path):
            persona_path = os.path.abspath("lml_persona.md")

        if os.path.exists(persona_path):
            with open(persona_path, "r", encoding="utf-8") as f:
                self.persona_content = f.read()
            if self.enable_logging:
                Logger.log("Persona file loaded successfully.")
        else:
            raise FileNotFoundError(f"Persona file not found. Check path: {persona_path}")

        # Load Factory LLM (Meta-AI architect engine)
        self.lml = LMLCore(self.ftllm_path)
        self.lml.load_model()

        # Load dataset using DatasetLoader
        loader = DatasetLoader(self.dataset_path)
        self.dataset = loader.load_data()

        if self.enable_logging:
            Logger.log(f"Dataset loaded successfully. Total items: {len(self.dataset)}", log_dir=self.log_dir)

    def run_factory_build(self, save_dir="result_model"):
        if self.enable_logging:
            Logger.log("Factory model build process started.", log_dir=self.log_dir)

        print(f"[i] Factory LLM build process has started. (Alpha Placeholder Mode)")

        os.makedirs(save_dir, exist_ok=True)
        # Execute model build pipeline
        self.lml.build_new_model(self.dataset, save_dir, persona=self.persona_content)

        if self.enable_logging:
            Logger.log("Logging successfully maintained.", log_dir=self.log_dir)

def print_custom_help():
    print("Usage:")
    print("  lml --dataset <path> --ftllm <path> --save_dir <path> --logging <path>")
    print("  lml help")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "help":
        print_custom_help()
        return

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--dataset", type=str, required=True, help="Path to the training dataset")
    parser.add_argument("--ftllm", type=str, required=True, help="Path to the Factory LLM base model")
    parser.add_argument("--save_dir", type=str, required=True, help="Directory to save the generated model")
    parser.add_argument("--logging", type=str, default=None, help="Directory path to save logs")

    args = parser.parse_args()

    # Run parameter recommendation analysis before starting engine
    target_params_b = analyze_and_recommend_parameters(args.dataset, args.ftllm)

    enable_logging = args.logging is not None
    log_dir = args.logging if enable_logging else "."

    engine = LMLEngine(
        dataset_path=args.dataset,
        ftllm_path=args.ftllm,
        output_path="output.jsonl",
        enable_logging=enable_logging,
        log_dir=log_dir
    )

    engine.run_factory_build(save_dir=args.save_dir)

if __name__ == "__main__":
    main()
