import os.path
import sys
from MAM import main


def test_initials():
    try:
        exists = os.path.exists("MAM.py")
        assert exists == True
    except:
        sys.exit()


    main()
