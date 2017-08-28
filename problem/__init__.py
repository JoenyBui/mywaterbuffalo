"""

The app goes through the Model-View-Controller Process

1. Models
    Model represent knowledge.

    Model in this case is the problem model.  The problem data can be something simple
    or complex data type - but it should not define any logic per se.


2. Views
    A view is a (visual) representation of it's model.

    View in our app is the html tags that we pass back to the front-end.  View can also
    be done outside the scope from other applications calling our controller.

3. Controllers
    A controller is the link between a user and the system.

    Controller in our app takes the model and returns it into consistent format for the view
    to render.  Controller is where the problem template turns into an instance of the problem.
"""