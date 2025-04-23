# ComfyUI-Poisson-Fusion

Professional image blending with Poisson seamless cloning for ComfyUI workflows

## Features
- **Seamless Image Fusion** - Advanced Poisson blending algorithm for natural-looking composites
- **Precise Mask Control** - Optional mask input for accurate blending boundaries
- **Offset Adjustment** - Fine-tune positioning with pixel-level precision
- **Workflow Integration** - Native ComfyUI node implementation with standard I/O

## Installation
1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
```bash
git clone https://github.com/yourusername/ComfyUI-poission_fusion.git
```
2. Restart ComfyUI


## Usage
1. **Node Structure**
```
[Source Image] --> PoissonFusion --> [Blended Result]
[Target Image] --/
      [Mask] --/
```

2. **Parameters**
| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| Source Image | IMAGE | - | Foreground element to blend |
| Target Image | IMAGE | - | Background plate |
| Mask | IMAGE | Optional | Blending region mask (default: full white) |
| Offset Left | INT | 0-2048 | Left offset adjustment |
| Offset Right | INT | 0-2048 | Right offset adjustment |
| Offset Up | INT | 0-2048 | Top offset adjustment |
| Offset Down | INT | 0-2048 | Bottom offset adjustment |

## Technical Details
**Algorithm**: Implements OpenCV's `seamlessClone` with `NORMAL_CLONE` mode

**Performance**:
- 1080p processing: <500ms (RTX 3080)
- Memory usage: <1GB per 4K image

## Compatibility
- ComfyUI 0.3.27
- Python 3.8-3.11
- Windows/Linux/macOS

## License
MIT License - See [LICENSE](LICENSE) for details
