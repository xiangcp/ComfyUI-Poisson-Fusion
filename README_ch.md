# ComfyUI-Poisson-Fusion

专业的图像融合工具，为ComfyUI工作流提供泊松无缝融合功能，很适合外扩图和内扩图的场景。

## 功能特性
- **无缝图像融合** - 先进的泊松融合算法，实现自然逼真的合成效果
- **精确遮罩控制** - 可选的遮罩输入，实现精准的融合边界控制
- **偏移调整** - 像素级精度的位置微调
- **工作流集成** - 原生ComfyUI节点实现，支持标准输入输出

## 安装指南
1. 将本仓库克隆到`ComfyUI/custom_nodes/`目录下：
```bash
git clone https://github.com/yourusername/ComfyUI-poission_fusion.git

2. 重启ComfyUI
## 使用说明
### 参数说明
假设输入图像为规则多边形，可以通过偏移量计算融合位置的中心点。

- 源图像 (IMAGE): 需要融合到目标图像的前景元素
- 目标图像 (IMAGE): 作为背景的图像，源图像将融合到该图像上
- 遮罩 (IMAGE, 可选): 融合区域遮罩（默认：全白遮罩）
- 左偏移 (INT, 0-2048): 左侧位置调整
- 右偏移 (INT, 0-2048): 右侧位置调整
- 上偏移 (INT, 0-2048): 顶部位置调整
- 下偏移 (INT, 0-2048): 底部位置调整
## 技术细节
算法 : 使用OpenCV的 seamlessClone 函数，采用 NORMAL_CLONE 模式

性能 :

- 1080p处理: <500ms (RTX 3080)
- 内存使用: <1GB每4K图像
## 兼容性
- ComfyUI 0.3.27
- Python 3.8-3.11
- Windows/Linux/macOS
## 许可证
MIT许可证 - 详见 LICENSE 文件