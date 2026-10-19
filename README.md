# LML (Let's Make LLM) - Alpha v0.1.0

> A meta-AI engine where a base model acts as an architect to design and build new model structures.

**Alpha Stage & Notice**: 
This project is currently in an early **Alpha phase**. Full autonomous training loops are under active development.

* **Windows Installer Note**: During a rapid OS migration to a Linux/Ubuntu environment and secure cloud backup (Proton Drive) quota management, legacy pre-compiled `.exe` binaries were omitted to prioritize core source code. However, the Inno Setup script (`setup.iss`) is included in the repository if you still wish to inspect or build it for Windows.

### Project Roadmap

*   **v0.1.0-alpha (Core Skeleton Architecture)**: Establishes the initial project structure, including CLI routing, dataset loading, system logging, and the basic training-pipeline skeleton.
*   **v0.2.0-alpha (AI-Assisted Model-Building Pipeline)**:
    *   **AI-Based Tokenizer Design and Code Generation**: Analyze the dataset and generate tokenizer implementation code suited to it.
    *   **Hardware-Aware Training Code Generation**: Generate training code based on the user's hardware specifications.
    *   **Independent AI Code Cross-Verification**: Use a separate verifier model to review the generated code.
    *   **Editable Installation**: Support `pip install -e .`.
    *   **Version Command**: Support `lml --version`.

---

## Installation (amd64 Ubuntu/Debian)

```bash
sudo apt install ./lml_0.1.0-alpha_amd64.deb
```

## Installation (amd64 Windows)

Pre-compiled `.exe` binaries are currently omitted. You can inspect or build the installer yourself using the provided Inno Setup script (`setup.iss`) with [Inno Setup 7.1.0](https://github.com/jrsoftware/issrc/releases/download/is-7_1_0/innosetup-7.1.0-x64.exe), or run the source code directly via Python.

# Usage (Example path: C:/users/user/Desktop/example)
```bash
lml --dataset <path> --ftllm <path> --save_dir <path> --logging <path>
```
