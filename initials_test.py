import os.path
import sys
from muhsonah import main


def test_initials():
    try:
        exists = os.path.exists("muhsonah.py")
        assert exists == True
    except:
        sys.exit()


    main()
