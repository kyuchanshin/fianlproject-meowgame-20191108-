# Meow Game - DDR (고양이 발자국 리듬 게임)

## 개요
**Meow Game - DDR**은 리듬 게임의 한 종류로, 고양이의 발자국과 음악에 맞춰 화살표를 누르는 게임입니다. 이 게임은 고양이 발자국의 모양을 따라 화살표를 누르는 리듬 게임으로, 정확한 타이밍에 화살표를 누를 때마다 플레이어는 점수를 얻습니다. 또한 게임을 진행하면서 고양이의 울음 소리와 함께 음악이 흘러갑니다.

**Meow Game - DDR** is a rhythm game in which players press arrow keys according to the shape of a cat's paw print and the music. In this game, squares turn yellow as the cat's paw print touches them, and players must press arrow keys to match the shape of the cat's paw print. Whenever arrows are pressed with precise timing, players earn points. The game also features cat meowing sounds that play as the game progresses.

## 게임 플레이
- 게임 화면에서 고양이 발자국이 아래로 내려옵니다.
- 발자국이 아래 사각형에 닿으면 해당 사각형이 노란색으로 칠해집니다.
- 플레이어는 고양이 발자국의 모양을 따라 화살표 방향을 눌러야 합니다.
- 정확한 타이밍에 화살표를 누를 때마다 10점을 획득하며 "perfect" 텍스트와 엄지를 세운 이모티콘이 표시됩니다.
- 화살표를 누를 때마다 고양이 울음 소리가 재생됩니다.
- 타이밍을 놓치고 화살표를 누르면 "terrible" 텍스트와 엄지를 내리고 있는 이모티콘이 표시됩니다.
- 플레이어의 기회(chance)가 0이 되면 게임이 종료됩니다.

## Gameplay
- In the game screen, cat paw prints come down.
- When the paw prints touch the square below, the square turns yellow.
- Players must press the arrow keys to match the shape of the cat's paw print.
- Pressing the arrow at the right time earns the player 10 points, and "perfect" text and a thumbs-up emoji are displayed.
- Cat meowing sounds play every time you press an arrow.
- If you miss the timing and press the arrow, the text "terrible" and a thumbs-down emoji are displayed.
- When the player's chances (chance) reach 0, the game ends.

## 중간 진행 상황
- 게임의 중간 진행 상황에 대한 코드 예시와 설명은 게임 개발 과정을 설명하고 있습니다.
- 화살표의 방향과 위치를 관리하는 변수, 화살표 이미지 로드 및 회전, 그리고 게임 루프 동안 화살표를 그리는 방법에 대한 설명이 포함되어 있습니다.

## Game Progress
- The code examples and explanations in the middle of the game describe the development process of the game.
- It includes explanations of variables that manage the direction and position of arrows, loading and rotating arrow images, and how arrows are drawn during the game loop.

## 발전 방향
1. 게임 레벨 조절 기능 추가
2. 정교한 타이밍에 따른 점수 시스템 개선
3. 아이템 시스템 추가하여 아이템을 획득할 때 게임 속도를 느리게 만드는 기능 구현

## Future Improvements
1. Implement a level adjustment feature to allow players to customize game difficulty.
2. Enhance the scoring system to provide more detailed score variations based on precise timing.
3. Create an item system that can slow down the game speed when collected.

# final DDR 리듬 게임

final DDR은 고양이 발자국과 음악을 이용한 리듬 게임입니다. 게임은 Python과 Pygame 라이브러리를 사용하여 만들어졌으며, 고양이 발자국이 화면 위에서 아래로 떨어질 때 화살표 키를 누르는 타이밍에 따라 점수를 획득하는 게임입니다. 게임의 목표는 최고 점수를 얻는 것이며, 플레이어는 타이밍을 놓치지 않고 화살표 키를 눌러야 합니다.

## 게임 화면

게임 화면은 다음과 같은 구성 요소로 이루어져 있습니다.

- 게임 배경: 고양이 테마의 배경 이미지가 표시됩니다.
- 화살표 발자국: 화살표 방향을 나타내는 고양이 발자국 이미지가 화면 위에서 아래로 떨어집니다.
- 타겟 영역: 화살표 발자국이 떨어지는 위치를 나타내는 사각형 영역입니다.
- 점수 및 생명 수: 현재 점수와 생명 수를 화면 상단에 표시합니다.

## 게임 규칙

- 화살표 발자국이 타겟 영역에 닿을 때 화살표 방향에 맞게 화살표 키를 누르세요.
- 정확한 타이밍에 화살표 키를 누르면 "perfect" 효과와 함께 10점을 획득합니다.
- 타이밍을 놓치고 화살표 키를 누르면 "terrible~~" 효과가 표시됩니다.
- 생명 수(chance)가 0이 되면 게임 오버되며, 스페이스바를 눌러 게임을 재시작할 수 있습니다.

## 코드 설명

### 게임 초기화 및 설정

- `pygame` 및 기타 초기 설정을 수행합니다.
- 게임 화면 크기, 배경음악 및 효과음을 설정합니다.

### 사운드 관련 함수

- `playMeowSound()`: 고양이 울음 소리를 재생합니다.
- `playPerfectSound()`: "perfect" 효과음을 재생합니다.

### 게임 화면 및 이벤트 처리

- `resultProcess(direction)`: 화살표 키 입력에 따른 결과를 처리합니다.
- `eventProcess()`: 이벤트 처리 함수로, 화살표 키 입력 및 게임 종료를 처리합니다.

### 화살표 객체 클래스 (Direction)

- 화살표를 나타내는 클래스입니다.
- 화살표의 초기 위치, 이미지, 회전, 그리기 및 위치 확인을 관리합니다.

### 화살표 및 타겟 영역 관련 함수

- `drawIcon()`: 화살표를 그리고 화면에 표시합니다.
- `draw_targetArea()`: 타겟 영역을 그리고 화면에 표시합니다.

### 화면 텍스트 표시 함수

- `setText()`: 현재 점수와 생명 수를 화면에 텍스트로 표시합니다.

### 게임 결과 및 메인 루프

- `drawResult()`: 게임 결과를 화면에 표시합니다.
- 게임 루프를 실행하고 화면을 업데이트합니다.

## 게임 실행 방법

1. Python 및 Pygame 라이브러리를 설치합니다.
2. 코드를 다운로드하고 `final_DDR.py` 파일을 실행합니다.
3. 게임이 시작되면 화살표 키를 사용하여 플레이합니다.
4. 최고의 점수를 얻는 것을 목표로 하세요!

# final DDR 리듬 게임

final DDR is a rhythm game that uses cat pawprints and music. The game is created using Python and the Pygame library, and the goal of the game is to score points by pressing the arrow keys in time with the falling cat pawprints. The objective of the game is to achieve the highest score, and players must press the arrow keys without missing the timing.

## Game Screen

The game screen consists of the following components:

- Game Background: A cat-themed background image is displayed.
- Arrow Pawprints: Cat pawprint images representing arrow directions fall from the top to the bottom of the screen.
- Target Area: A rectangular area indicates where the arrow pawprints should be pressed.
- Score and Lives: The current score and number of lives (chance) are displayed at the top of the screen.

## Game Rules

- Press the arrow keys in time with the falling arrow pawprints when they reach the target area.
- Pressing the arrow keys with perfect timing will earn you 10 points and display a "perfect" effect.
- If you miss the timing and press the arrow keys, a "terrible~~" effect will be shown.
- When the number of lives (chance) reaches 0, the game is over, and you can restart the game by pressing the spacebar.

## Code Explanation

### Game Initialization and Settings

- Initialize `pygame` and perform other initial settings.
- Set the game screen size, background music, and sound effects.

### Sound-related Functions

- `playMeowSound()`: Plays the sound of a cat's meow.
- `playPerfectSound()`: Plays the "perfect" sound effect.

### Game Screen and Event Handling

- `resultProcess(direction)`: Handles the result based on arrow key input.
- `eventProcess()`: An event handling function that processes arrow key input and game exit.

### Arrow Object Class (Direction)

- Represents the arrows in the game.
- Manages the initial position, image, rotation, drawing, and position checking of the arrows.

### Functions Related to Arrows and the Target Area

- `drawIcon()`: Draws the arrows and displays them on the screen.
- `draw_targetArea()`: Draws the target area and displays it on the screen.

### Screen Text Display Function

- `setText()`: Displays the current score and number of lives as text on the screen.

### Game Result and Main Loop

- `drawResult()`: Displays the game result on the screen.
- Runs the game loop and updates the screen.

## How to Run the Game

1. Install Python and the Pygame library.
2. Download the code and run the `final_DDR.py` file.
3. Play the game using the arrow keys.
4. Aim for the highest score!


## 시연 영상
[Watch Demo Video](https://www.youtube.com/watch?embeds_referring_euri=http%3A%2F%2Fcyber.sogang.ac.kr%2F&source_ve_path=MTY0NTAz&feature=emb_share&v=-GqjCy1jnQQ)

## 트레일러 영상
[Watch Trailer Video](https://youtu.be/cNAJi0kEwDc)
