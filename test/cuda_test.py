import torch

# Check if CUDA (GPU) is available
if torch.cuda.is_available():
    print("CUDA (GPU) is available.")
    
    # Check for CuDNN availability
    if torch.backends.cudnn.is_available():
        cudnn_version = torch.backends.cudnn.version()
        print(f"CuDNN Version: {cudnn_version}")
    else:
        print("CuDNN is not available.")
else:
    print("CUDA (GPU) is not available.")

