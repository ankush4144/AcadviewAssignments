class MovieDetails:
    def __init__(self,artistName,yearOfRelease,ratings):
        self.name=artistName
        self.year=yearOfRelease
        self.ratings=ratings
    
    def Add(self,movieName):
        self.movieName=movieName
    def Display(self):
        print(self.name)
        print(self.year)
        print(self.ratings)
        print(self.movieName)
details=MovieDetails("TOM CRUISE",2018,9.0)
details.Add(input("Enter Movie Name : "))
details.Display()
