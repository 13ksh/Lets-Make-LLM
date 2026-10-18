# LML (Let's Make LLM) - Alpha v0.1.0

> A meta-AI engine where a base model acts as an architect to design and build new model structures.

**Alpha Stage & Notice**: 
This project is currently in an early **Alpha phase**. Full autonomous training loops are under active development.

* **Windows Installer Note**: During a rapid OS migration to a Linux/Ubuntu environment and secure cloud backup (Proton Drive) quota management, legacy pre-compiled `.exe` binaries were omitted to prioritize core source code. However, the Inno Setup script (`setup.iss`) is included in the repository if you still wish to inspect or build it for Windows.

### Project Roadmap & Architecture Strategy

This project strictly follows the **Skeleton Architecture** paradigm. Version 0.1.0 focuses on validating the unified End-to-End pipeline (Hardware auto-detection, Tokenization, and Training/Trainer connection loops).

*   **v0.1.0-alpha (Current)**: Core Skeleton Engine Validation (CLI Router, Dataset Pipeline, System Logging).
*   **v0.2.0-alpha (Next)**: 
    *   **LLM-as-a-Judge Orchestration**: Implementing a real-time feedback loop where the `ftllm` acts as an automated inspector to evaluate training loss/responses and trigger early stopping.
    *   **Lightweight Training**: Integrating PEFT (LoRA) and BitsAndBytes 4-bit/8-bit quantization to drastically reduce heavy LLM-to-LLM training footprints.

---

## Installation (amd64 Ubuntu/Debian)

```bash
sudo apt install ./lml_0.1.0-alpha_amd64.deb
```

## Installation (amd64 Windows)

Pre-compiled `.exe` binaries are currently omitted. You can inspect or build the installer yourself using the provided Inno Setup script (`setup.iss`) with [Inno Setup 7.1.0](https://github.com/jrsoftware/issrc/releases/download/is-7_1_0/innosetup-7.1.0-x64.exe), or run the source code directly via Python.

# Usage (ex. C:/users/user/Desktop/example)
```bash
lml --dataset <path> --ftllm <path> --save_dir <path> --logging <path>
```
