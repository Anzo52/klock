# The class myApp inherits from the App class. The class myApp has a function build() that returns a
# layout that contains a myClock object and a Label object.
import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout

# Setting the size of the window to 400x700 pixels.
Window.size = (400, 700)

# The class myClock inherits from the Label class and has a method called update that updates the
# time.
class myClock(Label):

    # Updating the time.
    def update(self, *args):
        self.text = time.asctime()

# The class myApp inherits from the App class. The class myApp has a function build() that returns a
# layout that contains a myClock object and a Label object.
class myApp(App):

    def build(self):
        """
        The function build() returns a layout that contains a myClock object and a Label object.
        :return: The layout is being returned.
        """
        layout = BoxLayout(orientation='vertical')

        my_clock = myClock()

        Clock.schedule_interval(my_clock.update, 1)

        layout.add_widget(my_clock)

        layout.add_widget(Label(text="Local Time"))

        return layout

# Creating an instance of the class myApp and calling the run() method on the instance.
root = myApp()
root.run()
