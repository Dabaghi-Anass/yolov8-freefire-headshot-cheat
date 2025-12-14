import cv2
import os
from pathlib import Path


VIDEOS = [
    "videos/B2KVIDEO.mp4",
    "videos/M8NVIDEO.mp4",
    "videos/WHITEFFVIDEO.mp4",
]

OUTPUT_DIR = "all_frames"
IMG_SIZE = 640        # 640x640
FRAME_STEP = 30

def extract_frames(video_path, output_dir, img_size=640, frame_step=60):
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), f"Cannot open video: {video_path}"

    video_name = Path(video_path).stem
    os.makedirs(output_dir, exist_ok=True)

    frame_id = 0
    saved_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_id % frame_step == 0:
            frame = cv2.resize(frame, (img_size, img_size))
            filename = f"{video_name}_{frame_id:06d}.jpg"
            cv2.imwrite(os.path.join(output_dir, filename), frame)
            saved_id += 1

        frame_id += 1

    cap.release()
    print(f"[OK] {video_name}: {saved_id} frames saved")


if __name__ == "__main__":
    for video in VIDEOS:
        extract_frames(
            video_path=video,
            output_dir=OUTPUT_DIR,
            img_size=IMG_SIZE,
            frame_step=FRAME_STEP
        )
