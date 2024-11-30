import tkinter as tk
from tkinter import ttk, messagebox

class DietPlanApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diet Plan Application")
        self.root.geometry("1000x700")  # Adjusted size to accommodate the design frame
        self.root.config(bg="#f0f8ff")  # Light blue background

        # Create a scrollable frame
        self.scroll_canvas = tk.Canvas(self.root, bg="#f0f8ff")
        self.scroll_canvas.pack(side="left", fill="both", expand=True)

        # Add a vertical scrollbar
        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.scroll_canvas.yview)
        self.scrollbar.pack(side="left", fill="y")

        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scroll_canvas.bind('<Configure>', lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

        # Frame inside the canvas
        self.main_frame = tk.Frame(self.scroll_canvas, bg="#f0f8ff")
        self.scroll_canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        # Design frame on the right side
        self.design_frame = tk.Frame(self.root, width=300, bg="#ffccbc", relief="raised", bd=2)
        self.design_frame.pack(side="right", fill="y")

        self.create_design_frame()

        # Define diet categories with food and their calorie values
        self.diets = {
            "Weight Loss": {
                "Food": {
                    "Salad": {"calories": 150, "protein": 5, "fat": 10, "carbs": 15},
                    "Chicken Breast": {"calories": 200, "protein": 35, "fat": 5, "carbs": 0},
                    "Tofu": {"calories": 180, "protein": 15, "fat": 10, "carbs": 5},
                    "Egg Whites": {"calories": 100, "protein": 20, "fat": 0, "carbs": 1},
                    "Broccoli": {"calories": 50, "protein": 3, "fat": 0, "carbs": 10},
                    "Spinach": {"calories": 40, "protein": 3, "fat": 0, "carbs": 7},
                    "Apple": {"calories": 95, "protein": 0, "fat": 0, "carbs": 25},
                    "Cucumber": {"calories": 16, "protein": 1, "fat": 0, "carbs": 4},
                    "Greek Yogurt": {"calories": 130, "protein": 10, "fat": 4, "carbs": 12},
                    "Almonds": {"calories": 160, "protein": 6, "fat": 14, "carbs": 6},
                }
            },
            "Weight Gain": {
                "Food": {
                    "Rice": {"calories": 200, "protein": 4, "fat": 1, "carbs": 45},
                    "Steak": {"calories": 400, "protein": 50, "fat": 25, "carbs": 0},
                    "Peanut Butter": {"calories": 180, "protein": 8, "fat": 16, "carbs": 6},
                    "Bananas": {"calories": 105, "protein": 1, "fat": 0, "carbs": 27},
                    "Avocado": {"calories": 250, "protein": 3, "fat": 22, "carbs": 12},
                    "Cheese": {"calories": 150, "protein": 10, "fat": 12, "carbs": 1},
                    "Eggs": {"calories": 160, "protein": 12, "fat": 10, "carbs": 1},
                    "Pasta": {"calories": 220, "protein": 7, "fat": 1, "carbs": 43},
                    "Nuts": {"calories": 200, "protein": 5, "fat": 18, "carbs": 7},
                    "Sweet Potato": {"calories": 180, "protein": 4, "fat": 0, "carbs": 41},
                }
            },
            "Muscle Gain": {
                "Food": {
                    "Chicken Breast": {"calories": 250, "protein": 45, "fat": 6, "carbs": 0},
                    "Quinoa": {"calories": 220, "protein": 8, "fat": 3, "carbs": 39},
                    "Salmon": {"calories": 300, "protein": 30, "fat": 20, "carbs": 0},
                    "Eggs": {"calories": 160, "protein": 12, "fat": 10, "carbs": 1},
                    "Greek Yogurt": {"calories": 130, "protein": 10, "fat": 4, "carbs": 12},
                    "Spinach": {"calories": 40, "protein": 3, "fat": 0, "carbs": 7},
                    "Almonds": {"calories": 160, "protein": 6, "fat": 14, "carbs": 6},
                    "Cottage Cheese": {"calories": 200, "protein": 20, "fat": 9, "carbs": 10},
                    "Sweet Potato": {"calories": 180, "protein": 4, "fat": 0, "carbs": 41},
                    "Lentils": {"calories": 200, "protein": 18, "fat": 1, "carbs": 35},
                }
            },
            "Vegan Diet": {
                "Food": {
                    "Tofu": {"calories": 180, "protein": 15, "fat": 10, "carbs": 5},
                    "Chickpeas": {"calories": 200, "protein": 15, "fat": 3, "carbs": 35},
                    "Quinoa": {"calories": 220, "protein": 8, "fat": 3, "carbs": 39},
                    "Broccoli": {"calories": 50, "protein": 3, "fat": 0, "carbs": 10},
                    "Spinach": {"calories": 40, "protein": 3, "fat": 0, "carbs": 7},
                    "Hummus": {"calories": 150, "protein": 5, "fat": 10, "carbs": 15},
                    "Avocado": {"calories": 250, "protein": 3, "fat": 22, "carbs": 12},
                    "Almonds": {"calories": 160, "protein": 6, "fat": 14, "carbs": 6},
                    "Oats": {"calories": 150, "protein": 6, "fat": 3, "carbs": 27},
                    "Sweet Potato": {"calories": 180, "protein": 4, "fat": 0, "carbs": 41},
                }
            }
        }

        self.create_registration_form()
        self.selected_diet = tk.StringVar()
        self.selected_meal = tk.StringVar()
        self.food_dropdown = None
        self.create_interface()

    def create_design_frame(self):
        tk.Label(self.design_frame, text="Stay Motivated!", font=("Arial", 16, "bold"), bg="#ffccbc").pack(pady=10)
        
        motivational_quotes = [
            "Believe you can and you're halfway there.",
            "Your health is your wealth.",
            "Eat better, not less.",
            "Success starts with self-discipline.",
        ]
        
        self.quote_label = tk.Label(self.design_frame, text=motivational_quotes[0], font=("Arial", 12), bg="#ffccbc", wraplength=250, justify="center")
        self.quote_label.pack(pady=10)

        change_quote_button = tk.Button(self.design_frame, text="Change Quote", command=lambda: self.change_quote(motivational_quotes), bg="#ff7043", fg="#ffffff")
        change_quote_button.pack(pady=10)

    def change_quote(self, quotes):
        current_text = self.quote_label.cget("text")
        next_index = (quotes.index(current_text) + 1) % len(quotes) if current_text in quotes else 0
        self.quote_label.config(text=quotes[next_index])

    def create_registration_form(self):
        self.registration_frame = tk.Frame(self.main_frame, bg="#f5f5f5")
        self.registration_frame.grid(row=0, column=0, padx=10, pady=10)

        tk.Label(self.registration_frame, text="Name:", font=("Arial", 12), bg="#ffffff").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.registration_frame, font=("Arial", 12), bg="#f2f2f2", bd=2, relief="solid")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.registration_frame, text="Age:", font=("Arial", 12), bg="#ffffff").grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.registration_frame, font=("Arial", 12), bg="#f2f2f2", bd=2, relief="solid")
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.registration_frame, text="Gender:", font=("Arial", 12), bg="#ffffff").grid(row=2, column=0, padx=5, pady=5)
        self.gender_combobox = ttk.Combobox(self.registration_frame, values=["Male", "Female", "Other"], font=("Arial", 12), state="readonly", width=17)
        self.gender_combobox.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.registration_frame, text="Goal:", font=("Arial", 12), bg="#ffffff").grid(row=3, column=0, padx=5, pady=5)
        self.goal_combobox = ttk.Combobox(self.registration_frame, values=["Weight Loss", "Weight Gain", "Muscle Gain", "Vegan Diet"], font=("Arial", 12), state="readonly", width=17)
        self.goal_combobox.grid(row=3, column=1, padx=5, pady=5)

        register_button = tk.Button(self.registration_frame, text="Register", command=self.register_user, bg="#ff7043", fg="#ffffff")
        register_button.grid(row=4, column=0, columnspan=2, pady=20)

    def register_user(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_combobox.get()
        goal = self.goal_combobox.get()

        if not name or not age or not gender or not goal:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        try:
            age = int(age)
            if age <= 0:
                messagebox.showerror("Error", "Age must be a positive number")
                return
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid age")
            return

        self.user_info = {"Name": name, "Age": age, "Gender": gender, "Goal": goal}
        messagebox.showinfo("Registration Successful", f"Welcome {name}! Your goal is {goal}.")
        self.show_diet_plan()

    def create_interface(self):
        tk.Label(self.main_frame, text="Welcome to your personalized diet plan!", font=("Arial", 16, "bold"), bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=10)

        goal_label = tk.Label(self.main_frame, text="Select Your Goal:", font=("Arial", 12), bg="#f5f5f5")
        goal_label.grid(row=2, column=0, padx=10, pady=5)

        goal_combobox = ttk.Combobox(self.main_frame, values=["Weight Loss", "Weight Gain", "Muscle Gain", "Vegan Diet"], font=("Arial", 12), state="readonly", width=30)
        goal_combobox.grid(row=3, column=0, padx=10, pady=5)

        goal_combobox.bind("<<ComboboxSelected>>", self.on_goal_selected)

        # Add buttons for functionality
        nutrition_button = tk.Button(self.main_frame, text="Show Nutrition Info", bg="#ff7043", fg="#ffffff", command=self.show_nutrition_info)
        nutrition_button.grid(row=6, column=0, pady=10)

        weekly_schedule_button = tk.Button(self.main_frame, text="Weekly Diet Schedule", bg="#ff7043", fg="#ffffff", command=self.show_weekly_schedule)
        weekly_schedule_button.grid(row=7, column=0, pady=10)

        diet_track_button = tk.Button(self.main_frame, text="Diet Track", bg="#ff7043", fg="#ffffff", command=self.diet_track)
        diet_track_button.grid(row=8, column=0, pady=10)

    def on_goal_selected(self, event):
        selected_goal = event.widget.get()
        self.selected_diet.set(selected_goal)
        self.display_food_items(selected_goal)

    def display_food_items(self, goal):
        self.selected_meal.set('')
        self.food_items_frame = tk.Frame(self.main_frame, bg="#f5f5f5")
        self.food_items_frame.grid(row=5, column=0, padx=10, pady=10)

        # Create a dropdown for selecting food item
        if self.food_dropdown:
            self.food_dropdown.destroy()

        food_items = list(self.diets[goal]["Food"].keys())
        self.food_dropdown = ttk.Combobox(self.food_items_frame, values=food_items, font=("Arial", 12), state="readonly", width=30)
        self.food_dropdown.grid(row=0, column=0, padx=5, pady=5)

    def show_nutrition_info(self):
        selected_food = self.food_dropdown.get()
        if selected_food:
            food_info = self.diets[self.selected_diet.get()]["Food"][selected_food]
            messagebox.showinfo("Nutrition Info", f"{selected_food}:\nCalories: {food_info['calories']} kcal\nProtein: {food_info['protein']}g\nFat: {food_info['fat']}g\nCarbs: {food_info['carbs']}g")
        else:
            messagebox.showerror("Error", "Please select a food item.")

    def show_weekly_schedule(self):
        # Create a window for weekly diet and exercise schedule
        weekly_window = tk.Toplevel(self.root)
        weekly_window.title("Weekly Schedule")
        weekly_window.geometry("500x500")

        tk.Label(weekly_window, text="Weekly Diet and Exercise Plan", font=("Arial", 14, "bold")).pack(pady=10)

        diet_schedule = [
            "Monday: Chicken Breast, Salad, Rice",
            "Tuesday: Steak, Broccoli, Sweet Potato",
            "Wednesday: Salmon, Quinoa, Spinach",
            "Thursday: Chicken Breast, Greek Yogurt, Sweet Potato",
            "Friday: Rice, Eggs, Broccoli",
            "Saturday: Tofu, Pasta, Spinach",
            "Sunday: Steak, Sweet Potato, Salad"
        ]


        for day in diet_schedule:
            tk.Label(weekly_window, text=day, font=("Arial", 12)).pack(pady=5)

        # Add exercise schedule
        exercise_schedule = [
            "Monday: Chest & Triceps",
            "Tuesday: Back & Biceps",
            "Wednesday: Cardio",
            "Thursday: Shoulders & Abs",
            "Friday: Full Body",
            "Saturday: Rest",
            "Sunday: Cardio"
        ]

        tk.Label(weekly_window, text="Exercise Plan", font=("Arial", 12, "bold")).pack(pady=10)
        for exercise in exercise_schedule:
            tk.Label(weekly_window, text=exercise, font=("Arial", 12)).pack(pady=5)

    def diet_track(self):
        # Create a window for diet tracking
        track_window = tk.Toplevel(self.root)
        track_window.title("Diet Track")
        track_window.geometry("500x500")

        tk.Label(track_window, text="Your Diet Track", font=("Arial", 14, "bold")).pack(pady=10)

        # Display selected diet information
        goal = self.selected_diet.get()
        if goal:
            tk.Label(track_window, text=f"Your Goal: {goal}", font=("Arial", 12)).pack(pady=5)

            for food_item, values in self.diets[goal]["Food"].items():
                food_info = f"{food_item}: {values['calories']} kcal, {values['protein']}g protein, {values['fat']}g fat, {values['carbs']}g carbs"
                tk.Label(track_window, text=food_info, font=("Arial", 12)).pack(pady=5)

        else:
            tk.Label(track_window, text="Please select a goal to track your diet.", font=("Arial", 12)).pack(pady=10)

# Run the application
root = tk.Tk()
app = DietPlanApp(root)
root.mainloop()

