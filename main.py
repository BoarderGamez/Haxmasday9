from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button, Label, Static
from textual.containers import Grid, Vertical, Center
from textual.reactive import reactive
from textual.containers import Grid
import datetime
from textual.screen import Screen
class DayScreen(Screen):
    gifts = {
    1: "Hamburger",
    2: "Cheeseburger",
    3: "Hotdog",
    4: "Pizza",
    5: "Ice cream",
    6: "Chocolate",
    7: "Cake",
    8: "Cookies",
    9: "Chocolate bar",
    10: "Chocolate chip cookies",
    11: "Chocolate milk",
    12: "Chocolate cake"
}       
    """Screen for a day of the advent calendar!"""
    CSS = """
    DayScreen {
        align: center middle;
    }
    
    #dialog {
        width: 50;
        height: auto;
        border: thick $primary;
        background: $surface;
        padding: 2;
        align: center middle;
    }
    
    #dialog Label {
        width: 100%;
        text-align: center;
        margin-bottom: 1;
    }
    
    #dialog Button {
        width: auto;
    }
    """
    def __init__(self, day: int) -> None:
        self.day = day
        super().__init__()
    
    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label(f"Here's what's in day {str(self.day)}: {self.gifts.get(self.day)}")
            with Center():
                yield Button("Close", id="close")

    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss()
        event.stop()
class AdventCalendarApp(App):
    """Textual calendar app"""
    theme = "catppuccin-latte"
    completed = reactive(0)
    
    CSS = """
    #counter {
        height: 1;
        width: 100%;
        background: $primary;
        text-align: center;
        color: $text;
    }
    
    Grid {
        grid-size: 4 3;
        grid-gutter: 1 2;
    }
    
    Grid Button {
        width: 100%;
        height: 100%;
    }
    
    Grid Button:hover {
        background: $secondary;
    }
    
    Grid Button.opened {
        background: $success;
    }
    """
    
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    START_DATE = datetime.date(2025, 12, 13)
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Grid():
            for day in range(1, 13):
                yield Button(str(day), id=f"day-{day}")
        yield Static(f"Days completed: 0/12", id="counter")
        yield Footer()
    
    def watch_completed(self, value: int) -> None:
        try:
            self.query_one("#counter", Static).update(f"Days completed: {value}/12")
        except Exception:
            pass
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        button = event.button
        day = str(button.label)
        unlock_day = self.START_DATE + datetime.timedelta(days=int(day) - 1)
        
        if datetime.date.today() < unlock_day:
            self.notify(f"You will be able to unlock day {day} on {unlock_day}")
            return None
        
        if not button.has_class("opened"):
            button.add_class("opened")
            self.completed += 1
        self.push_screen(DayScreen(int(day)))

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "catppuccin-frappe" if self.theme == "catppuccin-latte" else "catppuccin-latte"
        )

def main():
    app = AdventCalendarApp()
    app.run()
    
if __name__ == "__main__":
    main()