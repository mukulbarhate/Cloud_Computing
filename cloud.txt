#getwd()
#setwd("D:/PG-DBDA CDAC/R/Day2")

#### Dataframe ####
# dataframe row column type, maxim manuipulat easily possible
?data.frame  # used to create data frames, 
?rm  # remove object from a specified environment u
data=c(1:69)
data
rm(data)

v=c(14,16,20,35)
v_2=c("Hello","Good night","Morning","Subha")

#Create dataframe with 2 columns: v & v_2
d_1<-data.frame(v,v_2);d_1

d_1<- data.frame(v,v_2,row.names = c('a','b','c','d'));d_1

rownames(d_1) = 1:4;d_1
class(d_1)
str(d_1)
diff(4,7) # dataframe should be of same length

dim(d_1)
row.names(d_1)[1]='xyx';d_1
row.names(d_1)[1:2]=c('O','P');d_1
row.names(d_1)[1]='e';d_1
row.names(d_1)[c(1,4)]=c('v','o');d_1

#d_1.head
?head
head(d_1)
View(d_1)
class(d_1)
str(d_1)
dim(d_1)

D=data.frame(XYZ=c(1,2,3,4),ABC=c('a','b','c','d'));D
names(D)<- c("FIRST",'SECOND');D
?data.frame


D[-c(2,4),]

a=c(2,"F");a
rbind(D,a)
?cbind
b=data.frame(XYZ=c(14,15),ABC=c('E','G'));b


D$XYZ=NULL;D
?head
# Change colnames of all columns
colnames(d_1)<- c('PQR',"STU");d_1


## 
fr_data=data.frame('id'=c(1:5),fr_name=c('a','b','c','d','e'),stringsAsFactors = T)
str(fr_data)
summary(fr_data)


fr_data$id
#expand a dataframe

fr_data$KGF = c('x','y','z','1','2');fr_data  # we have added the column extend
#names(d_1)[3] = 'Employee'
names(d_1)
letters[2:7]
rep('shruti',7)
# Reordering the dataframe by column number
fr_data[c(2,3,1)]
names(fr_data)
# Reordering the dataframe by column name
d <- fr_data[c('fr_name','KGF','id')];d


# Add new column 
d_1$Employee <- c('1','2','3','4');d_1
d_1$Employee_New <- c(1,2,3,4);d_1
str(d_1) # to check structure of dataframe

# Change colname

# Create a dataframe which has 3 columns & 10 rows column1 is serial no column 2 is name of the item
# column 3 is qunatity purchase add 4th column price of one quantity add 5th column total price
# if 20% discount is given then add column of new price
?prod

P=data.frame('id'=c(1:5),items=c('Pen','book','pencil','notebook','marker'), quantity=c(1,2,1,2,3));P
P$Price=c(20,30,10,20,30);P
P$Total_Price = P$quantity*P$Price;Price  # P$Price:- to get the Price from P
P$new_price=P$Total_Price*0.8;P


# Missing values
x=c(NA,5,3)
y=c(4,5,9)
z=c(1,22,NA)

d7= data.frame(x=x,y=y,z=z,stringsAsFactors = T);d7
#d7= data.frame(x=x,y=y,z=z);d7

d8=data.frame(x,y,z);d8

is.na(d7)
is.na(d7$x)
sum(is.na(d7$x))
sum(d7)
sum(d7, na.rm=T)
cleaned_data = na.omit(d7);cleaned_data
sum(cleaned_data)

#####
data("iris")
View(iris)
head(iris)
tail(iris)

data=iris
getwd()
data1= read.table("D:/PG-DBDA CDAC/R/Day2/data/Titanic_space_separated.txt")
# Check the statisitical summary of a dataset
summary(data1)

data1

authors <- data.frame(
  surname = I(c("Tukey", "Venables", "Tierney", "Ripley", "McNeil")),
  nationality = c("US", "Australia", "US", "UK", "Australia"),
  deceased = c("yes", rep("no", 4)))

?I # it will protect your that vector 2 character it will be easy to merge

books <- data.frame(
  name = I(c("Tukey", "Venables", "Tierney",
             "Ripley", "Ripley", "McNeil", "R Core")),
  title = c("Exploratory Data Analysis",
            "Modern Applied Statistics ...",
            "LISP-STAT",
            "Spatial Statistics", "Stochastic Simulation",
            "Interactive Data Analysis",
            "An Introduction to R"),
  other.author = c(NA, "Ripley", NA, NA, NA, NA,
                   "Venables & Smith"))

authors
books

(m1 <- merge(authors, books, by.x = "surname", by.y = "name"));m1

# Example to manipulate a dataframe 

salesreport<-data.frame(Id=101:110,
                        Product=c("A","B"),
                        Unitprice=as.integer(runif(10,100,200)),
                        Qty=as.integer(runif(10,10,20))
)
salesreport

#1.Transpose data frame
transpose.salesreport<-t(salesreport)
View(transpose.salesreport)
head(transpose.salesreport)
?t

#2.Sorting of data frame
salesreport[order(salesreport$Unitprice),]
salesreport[order(salesreport$Unitprice,decreasing = T),]

salesreport[order(salesreport$Product,-salesreport$Unitprice),]

#3.Subsetting data frame

subset.ProductA<-subset(salesreport,Product=="A")
subset.ProductA

# Extact the rows for which Product is A and Unitprice > 150
subset.salesreport<-subset(salesreport,Product=="A" & Unitprice>150)
subset.salesreport

# Extract only the first and the fourth column Product is A and Unitprice > 150
subset.salesreport<-subset(salesreport,Product=="A" & Unitprice>150,c(1,4))
subset.salesreport

#4.Merging of data frame

setA<-subset(salesreport,Product=="A")
setB<-subset(salesreport,Product=="B")
setA
setB
cbind(setA,setB)
rbind(setA,setB)

#5.Aggregate function
#Total quantity sold for each product

aggregate(salesreport$Qty,list(salesreport$Prod),sum,na.rm=T)

# You have data on the sales of different products in three different regions. 
#Each row represents the sales data for one product in one region. 
#You need to perform the following tasks:Read the data from a CSV file named 
#"sales_data.csv" into a dataframe.Display the structure of the dataframe.
#Calculate and display the total sales for each region.Calculate and display 
#the average sales for each product across all regions.Export the dataframe with 
#the calculated total and average sales to a new CSV file named "sales_summary.csv"

#1. read sales data
#2. Display the structure 
#3. calculate total sale for each country
#4. create new dataframe with 2 column countryname and total sale and export this dataframe

install.packages("openxlsx")
library(openxlsx)

data<- read.csv('D:/PG-DBDA CDAC/R/Day2/data/sales_data.csv');data
head(data)
str(data)
names(data)

aggregate(data$Revenue,list(data$Country),sum,na.rm=T)
total_sale=aggregate(Revenue~Country, data=data,FUN = sum);total_sale

# List R object which contain elements of different type like - numbers, string, vectors and another list
# inside it. A list can also contain a matrix or a function as its elements.
# list is created using list() function

# Create a list containing strings, no, vectors, and logical
list_data <- list('red','green',c(22,32,65),TRUE,45.3,45.3);list_data
length(list_data)

#Naming List element
list_data <- list(c('Jan','Feb','Mar'),matrix(c(3,9,5,1,-2,8),nrow = 2),list('green',12.3));list_data
list_data=list(I_Quater=c('Jan','Feb','Mar'),A_Matrix=matrix(c(3,9,5,1,-2,8),nrow = 2),A_Inner_list=list('green',12.3))
list_data=list(I_Quater<-c('Jan','Feb','Mar'),A_Matrix=matrix(c(3,9,5,1,-2,8),nrow = 2),A_Inner_list=list('green',12.3)) # will not take this and assign the value

names(list_data)
list_data$I_Quater  # $ will not consider the symbol <- when assignin but it will take = 
list_data$A_Matrix

list_data$A_Matrix[1,]
list_data$A_Matrix[1,1]

list_data[1]
list_data[1][1]

list_data[[1]]
list_data[[1]][1]
list_data[[1]][2]
list_data[[1]][3]

list_data[2]
list_data[[2]][1]
list_data[[2]][2]
list_data[[2]][3]

# factor are used the data object which are used to categorize the data & store it as levels.
# they can store both strings and integers. They are useful in the columns which have a limited number of unique values
# Like "Male","Female" and True, false etc. they are 

?factor
#create a vector as input
data=c('East','West','East',"North",'East')
print(data)

print(is.factor(data))

#Apply the factor function
factor_data <- factor(data);factor_data   # it arrange levels in Alphabetical orders
class(factor_data)
print(is.factor(factor_data))

# Factors as Data_Frame
#creae the vectors for data frames
height<-c(132,153,168,156,144,147)
weight<-c(45,78,56,54,55,45)

gender<-c('male','female','female','male','male','male')
?as.factor
# Create the data frame
input_data <- data.frame(height,weight,gender);input_data
str(input_data)

# Test if the gender column is a factor
print(is.factor(input_data$gender))
input_data$gender=as.factor(gender)
as.factor(gender)

#Changing the labels
input_data$gender=factor(input_data$gender,levels=c("male","female"),labels=c("m","f"));input_data
input_data$gender=factor(input_data$gender,levels=c("male","female"),labels=c("male","female"))
#Print the gender column so see the levels
print(input_data$gender)

#Changin the order of levels
data <- c('East','West',"North","West","North","West")
# create the factors
factor_data<-factor(data);factor_data

#Apply the factor fuction with required order of the level.
new_order_data <- factor(factor_data,levels=c('West','North','East'));new_order_data

#generating factor_lables
?gl  # syntax gl(n,k,labels)

v<-gl(3,4,labels = c("Tampa",'Seattke','Boston'));v


########### Control Statement ##
#R is case sensitive as well as space sensitive 
#if condition for one statement
#paste to concanate the string
x<-2
if (x>0) {
  print(paste(x," is positive"))
}

#if-else

x<-0
if (x>0) {
  print(paste(x,'is positive'))
}else{
  print(paste(x,'is negative'))
}

# Take integer input from user and check wheather it is positive or negative

num<-as.integer(readline())
if (num>0) {
  print(paste(num,'is positive'))
}else{
  print(paste(num,'is negative'))
}

# if else if
x <- 78
class(x)
if (x>0) {
  print(paste(x,'is positive'))
}else if(x<0){
  print(paste(x,'is negative'))
}else{
  print(paste(x,'is neither +ve nor -ve'))
}


# complex number
x<--5
is.complex(x)
if (is.complex(x) == TRUE) {
  print("It is complex")
}else{
  if(x>0){
    print("+ve")
  }else if (x<0){
    print("-ve")
  }else{
    print("zero")
  }
}
print(x)


# check wheather the no is even odd using control statement
n <- as.integer(readline())
if (n%%2 == 0) {
  print(paste(n,"is even no"))
}else{
  print(paste(n,"is odd no"))
}

#FOR statement 
for (q in 1:10) {
  print(q)
}

# print multiplication table of 7 upto 7*22
x=(1:22)
for (i in x) {
  print(7*i)
}

x=(1:10)
for (i in x) {
  print(paste(7,'x',i,'=',7*i))
}

names<-c('Peter','Harry','Ron','Hagrid')
for (name in names) {
  print(paste("Hello",name))
}

#Calculate sum of square for first 20 positive integer
sum=0
for (i in 1:20) {
  sum=sum+i**2
}
print(sum)

# Take integer
num<-as.integer(readline("Enter ur num: "))
if (num>0) {
  fact=1
  for (i in 1:num) {
    fact=i*fact
  }
  print(paste("Factorial is: ",fact))
}else if (num<0) {
  print("No factorial for negative no")
}else{
  print(paste(num," has factorial 0"))
}
#over that sequence
#WHILE condition
#run till the condition is TRUE
x=2
while (x<=5) {
  print(x)
  x=x+1
}
num=1
while (num<=22) {
  
}

# Print multiplication table of 7 upto 7*22 using while loop



#factor###############dataValidation()#factor####################################################################################
height <- c(132,151,162,139,166,147,122)
weight <- c(48,49,66,53,67,52,40)
gender <- c("male","male","female","female","male","female","male")
?as.factor

#create a data frame
input_data <- data.frame(height,weight,gender)
print(input_data)
str(input_data)

#test if the gender column is a factor
print(is.factor(input_data$gender))
input_data$gender=as.factor(gender)
as.factor(gender)


#changing labels
input_data$gender=factor(input_data$gender,levels=c("male","female"),labels=c("M","F"))

#print the gender column so see the levels
print(input_data$gender)












v <- c(14,26,38,30)
v_2 <- c("hello","Good Moring","Nice to meet you", "Me too")

# Create data frame with 2 columns : v and v_2
D_1 <- data.frame(v,v_2)
D_1

#row.names is used to gives the names to row of dataframe
D_1 <- data.frame(v,v_2, row.names = c("A","B",'C','D'))
D_1


rownames(D_1) <- 1:4
D_1

class(D_1)
typeof(D_1)

str(D_1)

row.names(D_1)[1]='abc'
row.names(D_1)[c(1,4)]=c('x','y')
D_1

head(D_1)
View(D_1)
class(D_1)
str(D_1)
dim(D_1)
D=data.frame(XYZ=c(10,11,12,13),ABC=c("A",'B','C','D'))
D

names(D) <- c("FIRST",'SECOND') #can allot the column names like this
colnames(D)  #to print the columns name

D[-c(1,2),]
a <- c(2,"F");a


rbind(D,a)
?cbind
b=data.frame(FIRST=c(14,15),SECOND=c('E','F'))

b$FIRST=as.factor(b$SECOND)
b$FIRST=as.factor(b$SECOND)
rbind(D,b)

D$FIRST
D$SECOND

#change the 
colnames(D_1) <- c("PQR",'STU')
D_1


#change the name of one columns



fr_data <- data.frame('id'= c(1:5),fr_name=c("A",'B','C','D','E'), stringsAsFactors = T)
str(fr_data)
summary(fr_data)

fr_data$id
#expand a dataframe

fr_data$KGF = c('X','Y','Z','1','2')
fr_data

names(D_1)[2] <- 'Employee'
D_1

letters[2:7]
rep("Shruti",7)

fr_data[c(2,3,1)]  #reordering the dataframe by column number, it doesn't affect og dataframe

fr_data

d <- fr_data[c('fr_name','KGF','id')]  ##reordering the dataframe by column number, it doesn't affect og dataframe
d

#add new column
D_1$Employee <- c('1','2','3','4')
D_1$Employee_New <- c(1,2,3,4)
D_1

str(D_1)


#create a data frame which has 3 col and 10 rows
#col 1 is serial num
#col2 is name of item
#col 3 is qty purchased

#add 4th col price of qty
#add 5th col total price
#if 20% discount is given then add col of new price


num <- c(1,2,3,4,5,6,7,8,9,10)
num

items <- c(LETTERS[1:10])
items

qty <- seq(10,1)
qty

mydataframe=data.frame(num,items,qty)
mydataframe

mydataframe$price <- c(1:10)
mydataframe

#total_price <- price*qty
#total_price

?prod

mydataframe
mydataframe$total_price<-mydataframe$price*mydataframe$qty  #we need to give ref
mydataframe

mydataframe$with_disc <- total_price*(0.80)
mydataframe
View(mydataframe)


#Missing Values
x =c(NA,2,3)

y= c(6,7,8)

z=c(10,11,NA)

newdata=data.frame(x=x,y=y,z=z)
newdata  #returns dataframe

is.na(newdata)  #returns dataframe with boolean with NA as True non-NA are false

is.na(newdata$x) #returns only first column 
is.na(newdata$y) ##returns only second column
is.na(newdata$z) ##returns only third column

sum(is.na(newdata$x))  #returns how many NA are available in first columns
sum(is.na(newdata$y))  #returns how many NA are available in second columns
sum(is.na(newdata$z))  #returns how many NA are available in third columns


sum(newdata) #by default na.rm is FALSE. i.e sum is 0
sum(newdata,na.rm = TRUE) #so by delaring na.rm is TRUE it ignores all NA and returns sum

sum(newdata$x,na.rm = T) #so by delaring na.rm is TRUE it ignores all NA and returns sum
sum(newdata$x) #by default na.rm is FALSE. i.e sum is 0
sum(newdata$y,na.rm = T) #so by delaring na.rm is TRUE it ignores all NA and returns sum
sum(newdata$y) 
sum(newdata$z,na.rm = T) #so by delaring na.rm is TRUE it ignores all NA and returns sum
sum(newdata$z)

newdata$k <- c(1,2,3)
newdata$k =NULL
newdata
newrow <- c(1,2,3)
myd <- rbind(newdata,newrow)
newrow
newdata
myd
sum(myd,na.rm = T)

cleaned_data= na.omit(myd);myd
cleaned_data
sum(cleaned_data)