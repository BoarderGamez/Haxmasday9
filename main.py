from textual.app import App, ComposeResult
from textual.widgets import Footer, Header, Button
from textual.containers import Grid

class AdventCalendarApp(App):
    """Textual calendar app"""
    
    CSS = """
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
    
    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Grid():
            for day in range(1, 13):
                yield Button(str(day), id=f"day-{day}")
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        button = event.button
        if not button.has_class("opened"):
            button.add_class("opened")
            day = button.label
            self.notify(f"Day {day} opened!")
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

def main():
    app = AdventCalendarApp()
    app.run()
    
if __name__ == "__main__":
    main()