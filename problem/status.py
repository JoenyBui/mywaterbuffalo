CREATED = 0
DRAFT = 1
SUBMITTED = 2
REVIEWED = 3
PUBLISHED = 4
REVISED = 5
LOCK = 6

STATUS_CHOICES = (
    (CREATED, 'Created'),
    (DRAFT, 'Draft'),
    (SUBMITTED, 'Submitted'),
    (REVIEWED, 'Reviewed'),
    (PUBLISHED, 'Published'),
    (REVISED, 'Revised'),
    (LOCK, 'Lock')
)

STATUS_DICT = {}
for id, value in STATUS_CHOICES:
    STATUS_DICT[id] = value
