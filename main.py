

from textual.app import App, ComposeResult
from textual.widgets import Footer, Header


class AdventCalendarApp(App):
    """A Textual app for an advent calendar!"""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()

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
