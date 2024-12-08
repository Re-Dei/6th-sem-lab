% Goal state
state(2, 0).

% Fill x
state(X, Y) :-
    X < 4,
    format("Fill the 4l jug: (~d, ~d)", [4, Y]),
    nl,
    state(4, Y).

% Fill y
state(X, Y) :-
    Y < 3,
    format("Fill the 4l jug: (~d, ~d)", [X, 3]),
    nl,
    state(X, 3).

% Empty x
state(X, Y) :-
    between(0, 4, X),
    format("Empty the 4l jug: (~d, ~d)", [0, Y]),
    nl,
    state(0, Y).

% Empty y
state(X, Y) :-
    between(0, 3, Y),
    format("Empty the 4l jug: (~d, ~d)", [X, 0]),
    nl,
    state(X, 0).

% Transfer x to y until y is full
state(X, Y) :-
    X+Y>=3,
    X>0,
    Y<3,
    New_X is X - (3-Y),
    format('Pour water from 4l jug to 3l until it is full: (~d, ~d)', [New_X, 3]),
    nl,
    state(New_X, 3).

% Transfer y to x until x is full
state(X, Y) :-
    X+Y>=4,
    Y>0,
    X<4,
    New_Y is Y - (4-X),
    format('Pour water from 3l jug to 4l until it is full: (~d, ~d)', [4, New_Y]),
    nl,
    state(4, New_Y).

% Transfer all contents of x to y
state(X, Y) :-
    X + Y =< 3,
    X>=0,
    Y=<3,
    New_Y is Y +X,
    format('Pour all water of 4l jug to 3l: (~d, ~d)', [0, New_Y]),
    nl,
    state(0, New_Y).

% Transfer all contents of y to x
state(X, Y) :-
    X + Y =< 4,
    Y>=0,
    X<4,
    New_X is Y +X,
    format('Pour all water of 4l jug to 3l: (~d, ~d)', [New_X, 0]),
    nl,
    state(New_X, 0).
