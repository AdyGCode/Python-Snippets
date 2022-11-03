class Pen:
    def __init__(self, name=None, ink_colour=None, pen_type=None):
        """
        Constructor - creates the instance of Pen

        :param name: string - name of the company
        :param ink_colour: string - the ink_colour of the pen's ink
        :param pen_type: string - the type/style of pen
        """
        self.name = name
        self.ink_colour = ink_colour
        self.pen_type = pen_type

    @property
    def name(self):
        """
        Name property getter
        
        :return: string - name of the pen 
        """
        return self._name

    @name.setter
    def name(self, pen_name):
        """
        Pen's manufacturer name property setter

        :param pen_name: string - the manufacturer's name
        """
        if pen_name is None:
            pen_name = "UNKNOWN"
        self._name = pen_name

    @property
    def ink_colour(self):
        """
        Pen ink colour property getter

        :return: string - the ink colour
        """
        return self._ink_colour

    @ink_colour.setter
    def ink_colour(self, pen_ink_colour):
        """
        Ink Colour setter, takes a string that is the colour of the
        pen's ink.

        If a none value given, then we set the ink colour to be UNKNOWN

        :param pen_ink_colour: string
        """
        if pen_ink_colour is None:
            pen_ink_colour = "UNKNOWN"
        self._ink_colour = pen_ink_colour

    @property
    def pen_type(self):
        """
        Pen Type property getter

        :return: string - the type of the pen 
        """
        return self._pen_type

    @pen_type.setter
    def pen_type(self, type_of_pen):
        """
        The setter for the pen's type.

        This takes a string that is the type of the pen. For example
        "roller ball", "fountain", "marker"...

        If a none value given, then we set the pen type to be UNKNOWN

        :param type_of_pen: string
        """
        if type_of_pen is None:
            type_of_pen = "UNKNOWN"
        self._pen_type = type_of_pen

    # A special DUNDER method:  DUNDER === DOUBLE UNDERscore.
    # Many dunder methods (eg __init__) that have specific purposes.
    # Others include __repr__, __gt__, __le__ and more.
    def __str__(self):
        """
        "To String" method that returns the pen in a pre-defined string
        form.

        Very useful to ensure consistent display of pen details.

        :return: string
        """
        return f"{self.ink_colour} {self.pen_type} pen by {self.name}"
