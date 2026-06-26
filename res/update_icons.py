import os
from PIL import Image

src_img_path = r"C:\Users\kayque.santos\.gemini\antigravity-ide\brain\6f13bedf-af00-4604-aa42-7e7ef71ea748\media__1781790453885.jpg"
root_dir = r"c:\Users\kayque.santos\Downloads\rustdesk-master\ampdesk-master"

# Open the source image
img = Image.open(src_img_path)

# List of PNG destinations and their target dimensions
png_targets = [
    (os.path.join(root_dir, "res", "128x128.png"), (128, 128)),
    (os.path.join(root_dir, "res", "128x128@2x.png"), (256, 256)),
    (os.path.join(root_dir, "res", "32x32.png"), (32, 32)),
    (os.path.join(root_dir, "res", "64x64.png"), (64, 64)),
    (os.path.join(root_dir, "res", "icon.png"), (256, 256)),
    (os.path.join(root_dir, "res", "mac-icon.png"), (512, 512)),
    (os.path.join(root_dir, "flutter", "assets", "logo.png"), (512, 512)),
    (os.path.join(root_dir, "flutter", "assets", "logo_dark.png"), (512, 512)),
    (os.path.join(root_dir, "flutter", "assets", "logo_light.png"), (512, 512)),
    (os.path.join(root_dir, "flutter", "assets", "icon.png"), (256, 256))
]

# Resize and save PNG files
for path, size in png_targets:
    print(f"Generating PNG: {path} ({size[0]}x{size[1]})")
    resized_img = img.resize(size, Image.Resampling.LANCZOS)
    resized_img.save(path, "PNG")

# List of ICO destinations
ico_targets = [
    os.path.join(root_dir, "flutter", "windows", "runner", "resources", "app_icon.ico"),
    os.path.join(root_dir, "res", "icon.ico"),
    os.path.join(root_dir, "res", "tray-icon.ico")
]

# Generate ICO files containing multiple sizes
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
for path in ico_targets:
    print(f"Generating ICO: {path}")
    # Prepare list of resized images for ICO
    ico_imgs = []
    for size in ico_sizes:
        ico_imgs.append(img.resize(size, Image.Resampling.LANCZOS))
    # Save the first image as ICO, appending the other sizes
    ico_imgs[0].save(path, format="ICO", sizes=ico_sizes, append_images=ico_imgs[1:])

print("All icons and logos updated successfully!")
