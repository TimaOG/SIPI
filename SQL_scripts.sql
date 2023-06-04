CREATE TABLE Users
(
	id serial PRIMARY KEY,
	userName varchar(255),
	userPassword text,
	email varchar(255),
	telegramId int,
	isMailing boolean,
	theme int,
	registrationDate date
);

CREATE TABLE Stocks
(
	id serial PRIMARY KEY,
	stockSymbol varchar(255)
);

CREATE TABLE Target_stocks
(
    Id SERIAL PRIMARY KEY,
    fkUser INTEGER,
    fkStock INTEGER,
    FOREIGN KEY (fkUser) REFERENCES Users (id),
    FOREIGN KEY (fkStock) REFERENCES Stocks (id)
);

create table Notifications (
    id serial primary key,
    fkTargetStock int,
    dealPrice float,
    useTelegram boolean,
    useEmail boolean,
    FOREIGN KEY (fkTargetStock) REFERENCES Target_stocks (id)
);
