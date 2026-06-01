import os.path
import sys
from mam import main


def test_initials():
    try:
        exists = os.path.exists("mam.py")
        assert exists == True
    except:
        sys.exit()


    main()
