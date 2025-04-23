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

### Parameters
Here, i assume that the input image is a regular polygon, so that the center point of the fusion position can be calculated using the offset.
- **Source Image** (IMAGE): Foreground element to blend into the target image
- **Target Image** (IMAGE): Background plate where the source image will be blended
- **Mask** (IMAGE, Optional): Blending region mask (default: full white mask)
- **Offset Left** (INT, 0-2048): Left offset adjustment for positioning
- **Offset Right** (INT, 0-2048): Right offset adjustment for positioning
- **Offset Up** (INT, 0-2048): Top offset adjustment for positioning
- **Offset Down** (INT, 0-2048): Bottom offset adjustment for positioning

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
