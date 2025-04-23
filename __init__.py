from .nodes import Poission_fusion
# 节点名字和Python类的映射
NODE_CLASS_MAPPINGS = {
    "Poission_fusion": Poission_fusion
}

# 节点的显示名字
NODE_DISPLAY_NAMES_MAPPINGS = {
    "Poission_fusion": "泊松融合"
}
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAMES_MAPPINGS']
