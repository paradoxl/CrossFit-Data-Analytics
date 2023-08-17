import pandas as pd
from matplotlib import pyplot
from sklearn.linear_model import LinearRegression
def fran_clean(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()


    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["candj"]
    benchmark = df_dropped["fran"] / 60

    lift_model = df_dropped[["candj"]]
    benchmark_model = df_dropped[["fran"]] / 60


    model.fit(lift_model,benchmark_model)



    #Scatter
    pyplot.title("Fran and clean and jerk correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,500)
    pyplot.ylim(0,15)
    pyplot.xlabel("Clean and Jerk")
    pyplot.ylabel("Grace")
    pyplot.savefig('static/images/fran_clean.png')
    weight = int(weight)
    return model.predict([[weight]])


def fran_dead(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()

    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["deadlift"]
    benchmark = df_dropped["fran"] / 60

    lift_model = df_dropped[["deadlift"]]
    benchmark_model = df_dropped[["fran"]] / 60

    model.fit(lift_model,benchmark_model)
    # print(model.predict([[100]]))

    pyplot.title("Fran and Deadlift correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,800)
    pyplot.ylim(0,15)
    pyplot.xlabel("Deadlift")
    pyplot.ylabel("Fran")
    pyplot.savefig('static/images/fran_dead.png')
    
    weight = int(weight)
    return model.predict([[weight]])   

def fran_snatch(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()


    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["snatch"]
    benchmark = df_dropped["fran"] / 60

    lift_model = df_dropped[["snatch"]]
    benchmark_model = df_dropped[["fran"]] / 60

    model.fit(lift_model,benchmark_model)
    # print(model.predict([[225]]))

    pyplot.title("Fran and Snatch correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,400)
    pyplot.ylim(0,15)
    pyplot.xlabel("Snatch")
    pyplot.ylabel("Fran")
    pyplot.savefig('static/images/fran_snatch.png')
    # pyplot.show()
    weight = int(weight)
    return model.predict([[weight]])


def grace_clean(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()
    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["candj"]
    benchmark = df_dropped["grace"] / 60

    lift_model = df_dropped[["candj"]]
    benchmark_model = df_dropped[["grace"]] / 60

    model.fit(lift_model,benchmark_model)
    # print(model.predict([[300]]))


    pyplot.title("Grace and clean and jerk correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,500)
    pyplot.ylim(0,15)
    pyplot.xlabel("Clean and Jerk")
    pyplot.ylabel("Grace")
    pyplot.savefig('static/images/grace_clean.png')
    weight = int(weight)

    return model.predict([[weight]])


# TODO figure out whats going on here with wonky prediction
def grace_dead(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()
    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift =df_dropped["deadlift"]
    benchmark = df_dropped["grace"] / 60

    lift_model = df_dropped[["deadlift"]]
    benchmark_model = df_dropped[["grace"]] / 60

    model.fit(lift_model,benchmark_model)
    #Something seems strange with this output.
    # print(model.predict([[400]]))


    pyplot.title("Grace and deadlift correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,800)
    pyplot.ylim(0,15)
    pyplot.xlabel("Deadlift")
    pyplot.ylabel("Grace")
    pyplot.savefig('static/images/grace_dead.png')
    weight = int(weight)

    return model.predict([[weight]])    

def grace_snatch(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()
    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["snatch"]
    benchmark =df_dropped["grace"] / 60

    lift_model = df_dropped[["snatch"]]
    benchmark_model = df_dropped[["grace"]] / 60

    model.fit(lift_model,benchmark_model)
    # print(model.predict([[255]]))

    pyplot.title("Grace and Snatch correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,500)
    pyplot.ylim(0,15)
    pyplot.xlabel("snatch")
    pyplot.ylabel("Grace")
    pyplot.savefig('static/images/grace_snatch.png')
    weight = int(weight)

    return model.predict([[weight]])


def helen_clean(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()

    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["candj"]
    benchmark = df_dropped["helen"] / 60

    lift_model = df_dropped[["candj"]]
    benchmark_model = df_dropped[["helen"]] / 60

    model.fit(lift_model,benchmark_model)
    # print(model.predict([[255]]))

    pyplot.title("Helen and Clean and Jerk correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,500)
    pyplot.ylim(0,25)
    pyplot.xlabel("Clean And Jerk")
    pyplot.ylabel("Helen")
    pyplot.savefig('static/images/helen_clean.png')
    weight = int(weight)
  
    return model.predict([[weight]]) 

def helen_dead(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()
    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["deadlift"]
    benchmark = df_dropped["helen"] / 60
    
    lift_model = df_dropped[["deadlift"]]
    benchmark_model = df_dropped[["helen"]] / 60

    model.fit(lift_model,benchmark_model)
    # print(model.predict([[255]]))

    pyplot.title("Helen and Deadlift correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,800)
    pyplot.ylim(0,25)
    pyplot.xlabel("Deadlift")
    pyplot.ylabel("Helen")
    pyplot.savefig('static/images/helen_dead.png')
    weight = int(weight)

    return model.predict([[weight]])


def helen_snatch(weight):
    df = pd.read_csv('athletes.csv')
    model = LinearRegression()
    #Dropping the missing rows.
    df_dropped = df.dropna()

    lift = df_dropped["snatch"]
    benchmark = df_dropped["helen"] / 60

    lift_model = df_dropped[["snatch"]]
    benchmark_model = df_dropped[["helen"]] / 60

    model.fit(lift_model,benchmark_model)
    # print(model.predict([[255]]))

    pyplot.title("Helen and Snatch correlation")
    pyplot.scatter(lift,benchmark)
    pyplot.xlim(0,400)
    pyplot.ylim(0,25)
    pyplot.xlabel("Snatch")
    pyplot.ylabel("Helen")
    pyplot.savefig('static/images/helen_snatch.png')
    weight = int(weight)

    return model.predict([[weight]])

