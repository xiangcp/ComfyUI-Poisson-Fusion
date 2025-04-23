
import cv2
import torch
import numpy as np
from PIL import Image

class Poission_fusion:
    """在图像融合的过程中使用泊松融合来，用于在ComfyUI中增强图像融合的效果"""
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "source_image": ("IMAGE",),    # 源图像，将被融合到目标图像中
                "target_image": ("IMAGE",),    # 目标图像，源图像将被融合到这个图像中
                # 使用类变量存储的当前keys
                "offset_left": ("INT",{
                    "default": 0,
                    "min": 0,
                    "max": 2048,
                    "step": 1
                }),
                "offset_right": ("INT",{
                    "default": 0,
                    "min": 0,
                    "max": 2048,
                    "step": 1
                }),
                "offset_up": ("INT",{
                    "default": 0,
                    "min": 0,
                    "max": 2048,
                    "step": 1
                }),
                "offset_down": ("INT",{
                    "default": 0,
                    "min": 0,
                    "max": 2048,
                    "step": 1
                })
            },
            "optional": {
                "mask": ("MASK",),
            },
            # 这样可以为 FUNCTION 提供 node_id 参数
            "hidden": { "node_id": "UNIQUE_ID" }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("IMAGE",)
    FUNCTION = "process"
    CATEGORY = "image/poission_fusion"

    def process(self, source_image, target_image, offset_left, offset_right, offset_up, offset_down, node_id, mask=None):
        try:
            source_image = source_image.movedim(-1,1)[0]
            target_image = target_image.movedim(-1,1)[0]

            # 将张量转换为PIL.Image
            source = Image.fromarray(np.clip(255. * source_image.movedim(0, -1).cpu().numpy(), 0, 255).astype(np.uint8))
            target = Image.fromarray(np.clip(255. * target_image.movedim(0, -1).cpu().numpy(), 0, 255).astype(np.uint8))

            # 处理掩码
            if mask is None:
                mask = np.ones((source.size[1], source.size[0]), dtype=np.uint8) * 255  # 使用.size获取尺寸
            else:
                mask = np.array(mask)
                if len(mask.shape) == 3:  # 如果是彩色图像
                    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
                mask = mask.astype(np.uint8)

            # 将PIL.Image转换为numpy数组
            source_np = np.array(source)
            target_np = np.array(target)

            # 计算融合区域
            x_start = offset_left
            x_end = target_np.shape[1] - offset_right
            y_start = offset_up
            y_end = target_np.shape[0] - offset_down

            # 计算中心点
            center = ((x_start + x_end) // 2, (y_start + y_end) // 2)

            # 进行泊松融合
            output = cv2.seamlessClone(source_np, target_np, mask, center, cv2.NORMAL_CLONE)

            # 将结果转换回张量格式
            output_tensor = torch.from_numpy(output.astype(np.float32) / 255.0).unsqueeze(0)
            return (output_tensor,)

        except Exception as e:
            print(f"Error: {e}")
            return (None,)  # 返回None而不是空字符串



