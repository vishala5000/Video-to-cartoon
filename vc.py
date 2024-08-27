import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def cartoonize_image(img):
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply median blur
    gray = cv2.medianBlur(gray, 7)
    # Edge detection
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                 cv2.THRESH_BINARY, 9, 10)
    # Apply bilateral filter to smooth color image
    color = cv2.bilateralFilter(img, 15, 75, 75)
    
    # Color quantization
    data = np.float32(color).reshape((-1, 3))
    k = 9
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    _, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    quantized = center[label.flatten()]
    quantized = quantized.reshape(color.shape)
    
    # Combine edges and quantized color image
    cartoon = cv2.bitwise_and(quantized, quantized, mask=edges)
    
    # Sharpen the cartoon image
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    cartoon = cv2.filter2D(cartoon, -1, kernel)
    
    return cartoon

def process_video(input_path, output_path):
    clip = VideoFileClip(input_path)
    def process_frame(frame):
        frame = cartoonize_image(frame)
        return frame
    cartoon_clip = clip.fl_image(process_frame)
    cartoon_clip.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    input_video = 'video.mp4'
    output_video = 'cartoon_video.mp4'
    process_video(input_video, output_video)
