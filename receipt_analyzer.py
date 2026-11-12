
import re
import csv
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# Tesseract installation path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Read receipt image
image = Image.open("receipt.jpg").convert("L")

# Improve image quality
image = ImageEnhance.Contrast(image).enhance(2)
image = image.filter(ImageFilter.SHARPEN)

# Extract text using OCR
text = pytesseract.image_to_string(image, config="--psm 6")

print("\n========== RECEIPT ANALYZER ==========\n")
print("EXTRACTED RECEIPT TEXT:\n")
print(text)

# Extract lines and prices
records = []
total_amount = None

price_pattern = r'(?<!\d)(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{1,2})?(?!\d)'

for line in text.splitlines():
    matches = re.findall(price_pattern, line)

    if matches:
        price = float(matches[-1].replace(",", ""))
        records.append([line.strip(), price])

        if re.search(r'\b(grand total|total|amount due|net amount|payable)\b',
                     line, re.IGNORECASE):
            total_amount = price

# Save extracted text
with open("receipt_text.txt", "w", encoding="utf-8") as file:
    file.write(text)

# Save extracted prices
with open("receipt_analysis.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Receipt Line", "Detected Amount"])
    writer.writerows(records)

print("\n========== ANALYSIS RESULTS ==========")
print("Price entries detected:", len(records))

if total_amount is not None:
    print("Detected Total Amount: Rs.", total_amount)
else:
    print("Total amount could not be identified automatically.")

print("\nFiles saved:")
print("1. receipt_text.txt")
print("2. receipt_analysis.csv")
print("\nANALYSIS COMPLETED!")
