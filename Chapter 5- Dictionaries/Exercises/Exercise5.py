## Exercise 5: Pets

pets = []

pet01 = {"kind": "\033[1mCub\033[1m", 
        "owner": "\033[1mRubyjane\033[1m"}
pet02 = {"kind": "\033[1mBunny\033[1m", 
        "owner": "\033[1mSooya\033[1m"}
pet03 = {"kind": "\033[1mChick\033[1m", 
        "owner": "\033[1mManobal\033[1m"}
pet04 = {"kind": "\033[1mHamster\033[1m", 
        "owner": "\033[1mRoseanne\033[1m"}
pet05 = {"kind": "\033[1mSnake\033[1m", 
        "owner": "\033[1mPark\033[1m"}


pets = [pet01, pet02, pet03, pet04, pet05]


for pet in pets:
    print ("\nAnimal Kind:", pet["kind"])
    print ("Owner's Name:", pet["owner"])
    print () 
