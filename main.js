//Имя игроков
const player1NameField = document.getElementById('player1-name');
const player2NameField = document.getElementById('player2-name');

//Слова игроков
const player1WordField = document.getElementById('player1-word');
const player2WordField = document.getElementById('player2-word');

const startBtn = document.getElementById('start-stop'); // Кнопка начала и останоки
const notificationField = document.getElementById('notifications'); // Поля для уведомлений
const gameWord = document.getElementById('generate-word'); // Поле, в котором написано основное слово игры
const wordsGuessedField = document.getElementById('words-guessed'); // Поле, в котором отображается кол-во оставшихся слов
const wordsList = document.getElementById('words-list'); // Список всех угаднных слов

// Таймеры для игроков
const player1TimerElement = document.getElementById('player1-timer');
const player2TimerElement = document.getElementById('player2-timer');
const playerTimer = document.getElementById('timer');

const defaultTimerTime = 420;

let player1TimeLeft = 420;       // Вот здесь точно let
let player2TimeLeft = 420;

let timerInterval = null;
let isGameStarted = false;

let player1Name = '';
let player2Name = '';

let isPlayer1Turn = true;

let gameWords = [];
let guessedWords = [];


// Обработчик событий при нажатии на кнопку "Timer"
playerTimer.addEventListener('click', handlePlayerTurn);

// Обработчик события при нажатии на кнопку "Start"
startBtn.addEventListener('click', startGame);

function startGame() {
  if (isGameStarted) {
    return;   
  }

  setPlayerNames();
  setWords();
  startBtn.parentNode.removeChild(startBtn);   
  isGameStarted = true;

  wordsList.innerHTML = '';   
  timerInterval = setInterval(decreasePlayer1Time, 1000);
  player1WordField.disabled = false;
}

// Выбери мне рандомные слова и устанави их
function setWords() {
  const randomWordSetIndex = Math.trunc(Math.random() * words.length);    

  const wordsSelected = words[randomWordSetIndex];
  gameWords = wordsSelected.slice(1);
  gameWord.innerHTML = wordsSelected[0];

  setGuessedWordsNotitification();  
}

// Запиши имена игроков и деактвируй поля для ввода имени
function setPlayerNames() {
  player1Name = player1NameField.value;
  player2Name = player2NameField.value;

  player1NameField.disabled = true;
  player2NameField.disabled = true;

  setNotification('Игра началась. Ход игрока 1');    
}

// Добавь слово в список угаданных слов
function addWordToHTMLList(word) {
  const liElement = document.createElement('li');
  liElement.innerHTML = word;

  wordsList.appendChild(liElement);
}

// Обработать ход игрока :))))
function handlePlayerTurn() {
  if (!isGameStarted) {
    return;
  }

  let playerField = null;

  if (isPlayer1Turn) {
    playerField = player1WordField;
  } else {
    playerField = player2WordField;
  }

  const word = playerField.value;

  if (handleWord(word)) {
    playerField.value = '';

    if (isAllWordsGueesed()) {          
      setGameover();
    } else {
      changePlayer();
    }
  } else {
    playerField.value = '';
  }
}

// Смени ход игрока, запиши слово игрока
function changePlayer() {
  clearInterval(timerInterval); // Сбрасываем предыдущий интервал, чтобы значение у таймера игрока перестало уменьшаться

  if (isPlayer1Turn) {
    timerInterval = setInterval(decreasePlayer2Time, 1000); // Устанавливаем интервал, который каждую секунду будет уменьшать количество оставшихся секунд у игрока 1
    setNotification('Ход Игрока 2');
  } else {                                                                   
    timerInterval = setInterval(decreasePlayer1Time, 1000); // Устанавливаем интервал, который каждую секунду будет уменьшать количество оставшихся секунд у игрока 2
    setNotification('Ход Игрока 1');
  }

  // Переключи поле для ввода игроков (одно выключается, другое включается, мэджик)
  player1WordField.disabled = isPlayer1Turn;
  player2WordField.disabled = !isPlayer1Turn;

  isPlayer1Turn = !isPlayer1Turn; // Сменяем ход игрока ура ура ура
}

// Уменьши таймер игрока 1
function decreasePlayer1Time() {
  player1TimeLeft = player1TimeLeft - 1;
  player1TimerElement.innerHTML = player1TimeLeft;

  if (player1TimeLeft <= 0) {
    setLoseGame();
    setNotification('Время вышло. Игрок 2 победил!');
  }
}

// ура копипастить наше все

// Уменьши таймер игрока 2
function decreasePlayer2Time() {
  player2TimeLeft = player2TimeLeft - 1;
  player2TimerElement.innerHTML = player2TimeLeft;

  if (player2TimeLeft <= 0) {
    setLoseGame();
    setNotification('Время вышло. Игрок 1 победил!');
  }
}

// Установи окончание игры
function setLoseGame() {
  clearInterval(timerInterval);
  setInitialState();
}

// Обработай слово от игрока
function handleWord(word) {    // обработай
  if (isValiableWord(word)) {  // проверь
    guessedWords.push(word.toLowerCase());
    addWordToHTMLList(word);
    setGuessedWordsNotitification();

    return true;
  } else {
    setNotification('Введите другое слово');   
    return false;
  }
}

// Проверка, что все слова угаданы
function isAllWordsGueesed() {
  return gameWords.length == guessedWords.length; 
}

// Проверь, если слово подходит
function isValiableWord(word) {
  word = word.toLowerCase();       // П - предусмотрительность!! 

  let isValiable = false;

  for (let i = 0; i < gameWords.length; i++) {
    if (gameWords[i] == word) {                    
      isValiable = true;
    }
  }                                           

                                            
  for (let i = 0; i < guessedWords.length; i++) {      

    if (guessedWords[i] === word) {
      isValiable = false;
    }                                             // это работает
  }

  return isValiable;           
}

// Установи сообщение в поле для уведомлений
function setNotification(message) {
  notificationField.innerHTML = message;
}

// Установи отгаданные слова
function setGuessedWordsNotitification() {     
  const numOfGuessedWords = guessedWords.length;
  const numOfTotalWords = gameWords.length;

  const fieldMessage = numOfGuessedWords + ' / ' + numOfTotalWords + ' угадано';

  wordsGuessedField.innerHTML = fieldMessage;
}

// Установи первоначальное состояние (готовность к игре)
// Просто сделай все "на ноль"
function setInitialState() {
  player1NameField.disabled = false;
  player2NameField.disabled = false;

  player1WordField.disabled = true;
  player2WordField.disabled = true;                   

  player1TimerElement.innerHTML = defaultTimerTime;
  player2TimerElement.innerHTML = defaultTimerTime;
  player1TimeLeft = defaultTimerTime;
  player2TimeLeft = defaultTimerTime;

  gameWords = [];
  guessedWords = [];

  isPlayer1Turn = true;
}

// Закончить игру  
function setGameover() {
  clearInterval(timerInterval);
  setNotification('Игра закончена!');
  isGameStarted = false;
  setInitialState();
}

mydiv = document.getElementById("showmehideme");

function showhide(d) {
    d.style.display = (d.style.display !== "none") ? "none" : "block";   // Work smarter. Steal code.
}

// красивое