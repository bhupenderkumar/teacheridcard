import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")
import os 
@app.route("/submit", methods=["POST"])
def submit():
  teacher_name = request.form["teacher_name"]
  class_ = 'PRE/NUR/LKG/UKG'
  husband_name = request.form["husband_name"]
  address = request.form["address"]
  designation = request.form["designation"]

  # Get the image filenames
  teacher_photo_name = request.files["teacher_photo"].filename
  husband_photo_name = request.files["husband_photo"].filename

  # Save the images to the image folder
  request.files["teacher_photo"].save(os.path.join("image", teacher_photo_name))
  request.files["husband_photo"].save(os.path.join("image", husband_photo_name))

  # Save the data to an Excel file
  with open("teachers.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([teacher_name, class_, husband_name, address, teacher_photo_name, husband_photo_name, designation])
  return "Teacher details submitted successfully!"
if __name__ == "__main__":
  app.run(host='0.0.0.0', port= 5004, debug=True)