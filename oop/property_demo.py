from decimal import Decimal


########################################################################
class Fees(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._fee = None
        self.username = None

    # ----------------------------------------------------------------------
    @property
    def fee_by(self):
        """
        The fee property - the getter
        """
        return self.username

    # ----------------------------------------------------------------------
    @fee_by.setter
    def fee_by(self, value):
        """
        The setter of the fee property
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


# ----------------------------------------------------------------------
if __name__ == "__main__":
    f = Fees()
    f.fee = '1'
    f.username = 'zz'
    print f.fee