import os
import pyJianYingDraft as draft
from pyJianYingDraft import trange, Clip_settings, Track_type

# 设置素材路径
tutorial_asset_dir = os.path.join(os.path.dirname(__file__), 'readme_assets', 'test')
video_path = os.path.join(tutorial_asset_dir, 'chanjing.mp4')
image_path = os.path.join(tutorial_asset_dir, '01.jpg')

# 创建剪映草稿
script = draft.Script_file(1080, 1080)

# 添加两个视频轨道，一个用于背景视频，一个用于图片
script.add_track(Track_type.video, "背景视频", relative_index=1)  # 底层轨道
script.add_track(Track_type.video, "图片层", relative_index=2)    # 上层轨道

# 导入视频素材
video_material = draft.Video_material(video_path)
script.add_material(video_material)

# 创建视频片段（使用完整视频长度）
video_segment = draft.Video_segment(
    video_material,
    trange("0s", video_material.duration)
)

# 导入图片素材
image_material = draft.Video_material(image_path)
script.add_material(image_material)

# 创建在视频10秒后显示的图片片段
image_segment = draft.Video_segment(
    image_material,
    trange("10s", "5s"),  # 从10秒开始，持续5秒
    clip_settings=Clip_settings(
        scale_x=0.8,     # 水平缩放到80%
        scale_y=0.8,     # 垂直缩放到80%
        transform_x=0,   # 水平居中
        transform_y=0    # 垂直居中
    )
)

# 添加片段到对应的轨道
script.add_segment(video_segment, "背景视频")  # 视频添加到背景轨道
script.add_segment(image_segment, "图片层")    # 图片添加到上层轨道

# 保存草稿到新地址
script.dump(r"C:\Users\Administrator\AppData\Local\JianyingPro\User Data\Projects\com.lveditor.draft\2月12日 (2)\draft_content.json")