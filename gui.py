import customtkinter as ctk
from nmap_scanner import nmap_scan
import threading
from auth import login, signup
from history import save_scan
from risk import analyze_risk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login – HackVault Lite")
        self.geometry("400x300")

        self.user = None

        ctk.CTkLabel(self, text="🔐 Login", font=("Consolas", 24)).pack(pady=20)

        self.username = ctk.CTkEntry(self, placeholder_text="Username")
        self.username.pack(pady=10)

        self.password = ctk.CTkEntry(self, placeholder_text="Password", show="*")
        self.password.pack(pady=10)

        ctk.CTkButton(self, text="Login", command=self.do_login).pack(pady=10)
        ctk.CTkButton(self, text="Signup", command=self.do_signup).pack()

    def do_login(self):
        ok, msg = login(self.username.get(), self.password.get())
        if ok:
            self.user = self.username.get()
            self.destroy()
        else:
            print(msg)

    def do_signup(self):
        signup(self.username.get(), self.password.get())


class CyberScannerGUI(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        self.username = username

        self.title("priyam bhai ka tool – Cyber Scanner")
        self.geometry("850x520")
        self.resizable(False, False)

        self.title_label = ctk.CTkLabel(
            self,
            text="🛡 priyam hacker",
            font=("Consolas", 28, "bold"),
            text_color="#00ff9c"
        )
        self.title_label.pack(pady=15)

        self.target_entry = ctk.CTkEntry(
            self,
            placeholder_text="Enter domain or IP (example.com)",
            width=420,
            font=("Consolas", 14)
        )
        self.target_entry.pack(pady=10)

        self.scan_button = ctk.CTkButton(
            self,
            text="START SCAN",
            font=("Consolas", 14, "bold"),
            fg_color="#00ff9c",
            text_color="black",
            command=self.start_scan
        )
        self.scan_button.pack(pady=10)

        self.output_box = ctk.CTkTextbox(
            self,
            width=780,
            height=300,
            font=("Consolas", 12),
            text_color="#00ff9c"
        )
        self.output_box.pack(pady=10)

        self.output_box.insert("end", ">>> Waiting for target...\n")
        self.output_box.configure(state="disabled")

    def start_scan(self):
        target = self.target_entry.get().strip()
        if not target:
            return

        self.output_box.configure(state="normal")
        self.output_box.delete("1.0", "end")
        self.output_box.insert("end", f">>> Scanning {target}...\n\n")
        self.output_box.configure(state="disabled")

        threading.Thread(target=self.run_scan, args=(target,), daemon=True).start()

    def run_scan(self, target):
        result = nmap_scan(target)
        save_scan(self.username, target, result)

        self.output_box.configure(state="normal")
        self.output_box.insert("end", result)
        self.output_box.configure(state="disabled")


if __name__ == "__main__":
    login_window = LoginWindow()
    login_window.mainloop()

    if login_window.user:
        app = CyberScannerGUI(login_window.user)
        app.mainloop()
