
from Src.PageObject.Pages.HomePage import Home
from Src.PageObject.Pages.SearchResultPage import SearchResult


def test_Search(Driver):

    Counter=1
    home = Home(Driver)
    SearchResultObj= SearchResult(Driver)
    home.AddSearchWord("lambdatest")
    home.PressSumbit()
    AssertionCheck=SearchResultObj.ReturnURLs()
    print(AssertionCheck)
    assert AssertionCheck == 1
