
from utilities.choices import ChoiceSet


class AccountStatusChoices(ChoiceSet):

    STATUS_RETIRED = 'retired'
    STATUS_ACTIVE = 'active'
    STATUS_PLANNED = 'planned'
    STATUS_DELETED = 'deleted'

    CHOICES = (
        (STATUS_RETIRED, 'Retired', 'orange'),
        (STATUS_ACTIVE, 'Active', 'green'),
        (STATUS_PLANNED, 'Planned', 'cyan'),
        (STATUS_DELETED, 'Deleted', 'gray'),

    )