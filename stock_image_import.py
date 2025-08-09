import random
from tkinter import Tk, filedialog
from PIL import Image

def analyze_stock_chart(image_path):
    try:
        img = Image.open(image_path)
        img.verify()
        print(f"✅ Loaded image: {image_path}")
    except Exception as e:
        print(f"❌ Error opening image: {e}")
        return

    # ---- Placeholder prediction (replace with AI model later) ----
    trend = random.choice(["UP 📈", "DOWN 📉"])
    change_percent = round(random.uniform(0.5, 5.0), 2)
    recommendation = "BUY ✅" if "UP" in trend else "SELL ❌"

    # ---- Output ----
    print("\n📊 Stock Prediction Result:")
    print(f"   Direction: {trend}")
    print(f"   Expected Change: {change_percent}%")
    print(f"   Recommendation: {recommendation}")

if __name__ == "__main__":
    # Hide the root Tkinter window
    root = Tk()
    root.withdraw()

    print("📂 Please select your stock chart image...")
    file_path = filedialog.askopenfilename(
        title="Select Stock Chart Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
    )

    if file_path:
        analyze_stock_chart(file_path)
    else:
        print("❌ No image selected.")
