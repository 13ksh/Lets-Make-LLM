import torch
import importlib.util

def get_device():
    # 1. NVIDIA (CUDA)
    if torch.cuda.is_available():
        return "cuda"

    # 2. AMD (ROCm)
    if hasattr(torch.version, 'hip') and torch.version.hip is not None:
        return "cuda"

    # 3. Intel (XPU)
    if importlib.util.find_spec("intel_extension_for_pytorch") is not None:
        if torch.xpu.is_available():
            return "xpu"

    # 4. CPU
    return "cpu"

DEVICE = get_device()
MODEL_PATH = "./model_weights"
MAX_LENGTH = 100
