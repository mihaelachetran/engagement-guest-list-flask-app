from flask import Flask, render_template, request
from guest_list import load_guests, save_guests

app = Flask(__name__)

VALID_RSVP = {"Pending", "Yes", "No"}

def clean_name(s: str) -> str:
    return(s or "").strip().lower()



def find_guest(guests, name: str):
    key = clean_name(name)
    return next((g for g in guests if clean_name(g.get("name")) == key), None)


@app.route("/", methods=["GET", "POST"])
def index():
    guests = load_guests()
    message = ""

    if request.method == "POST":
        action = request.form.get("action")
        name = request.form.get("guest_name", "").strip()

        if action == "add":
            if not name:
                message = "Guest name cannot be empty."
                
            elif find_guest(guests, name):
                message = "Guest already exists."
            else:
                guests.append({"name": name,"rsvp": "Pending"})
                save_guests(guests)
                message = f"{name} added successfully."

           
        elif action == "remove":
            guest = find_guest(guests, name)
            if guest:
                guests.remove(guest)
                save_guests(guests)
                message = f"{guest["name"]} removed successfully."
            else:
                message = f"{name} not found."

        elif action == "rsvp":
            rsvp_value = request.form.get("rsvp_value", "").strip()
            guest = find_guest(guests, name)

            if not guest:
                message = f"{name} not found."
            elif rsvp_value not in VALID_RSVP:
                message = "Invalid RSVP value."
            else:
                guest["rsvp"] = rsvp_value
                save_guests(guests)
                message = f"{guest["name"]}'s RSVP updated to {rsvp_value}."
    total = len(guests)
    confirmed = sum(1 for g in guests if g.get("rsvp") == "Yes")



    return render_template(
        "index.html",
        guests=guests,
        total=total,
        confirmed=confirmed,
        message=message
    )



if __name__ == "__main__":
    app.run(debug=True)