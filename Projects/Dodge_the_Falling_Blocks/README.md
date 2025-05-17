
# 🎮 Dodge the Chaos

**Dodge the Chaos** is a progressively challenging arcade-style survival game built with Python and Pygame. The player must dodge falling and flying hazards like bricks, bombs, cars, planes, and pianos as the game gets tougher based on the score. This project demonstrates core game development concepts such as sprite handling, dynamic difficulty, object collision, and state persistence.

---

## 🧩 Game Features

- ✅ Sprite-based player and falling objects
- 🎯 Dynamic difficulty scaling based on score
- 🔀 Predictable and unpredictable object behavior
- 💾 High score saving between sessions
- 🖼️ Rich graphics with custom assets
- 🎮 Smooth controls and responsive gameplay

---

## 🖥️ Requirements

- Python 3.7+
- [Pygame](https://www.pygame.org/) (Install with `pip install pygame`)

---

## 📂 Folder Structure

```
dodge_the_chaos/
├── dodge_game.py             # Main game file
├── highscore.txt             # Stores high score
├── assets/                   # Image assets
│   ├── player.png
│   ├── brick.png
│   ├── car.png
│   ├── bomb.png
│   ├── piano.png
│   └── plane.png
└── README.md
```

---

## 🕹️ How to Play

- Use the **Left** and **Right** arrow keys to move the player.
- Avoid all falling and flying objects.
- Score points for each object successfully avoided.
- The game difficulty increases as your score rises.
- If you collide with any object, the game ends.
- Your highest score is saved automatically.

---

## 📦 Setup & Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/dodge-the-chaos.git
cd dodge-the-chaos
```

### 2. Install Pygame

```bash
pip install pygame
```

### 3. Add Assets

Place the following `.png` files in the `assets/` directory:

- `player.png`
- `brick.png`
- `car.png`
- `bomb.png`
- `piano.png`
- `plane.png`

Recommended size: `40x40 px` for objects, `50x50 px` for player (with transparent background).

### 4. Run the game

```bash
python dodge_game.py
```

---

## 🔄 Game Logic Breakdown

### 🎮 Player Movement

The player moves left/right using arrow keys and is bounded within the screen edges.

### 🧱 Object Types

| Type             | Behavior            | Trigger (score) |
|------------------|---------------------|-----------------|
| Falling objects  | Predictable vertical drop | 0–11 points     |
| Faster falling   | Quicker drop, more frequent | 12–29 points   |
| Crazy objects    | Zigzag/random paths | 30+ points      |

### 💥 Collision Detection

- Objects are stored as rectangles (`pygame.Rect`)
- If any object’s rectangle intersects with the player’s rectangle → Game Over

### 📈 Difficulty Progression

```python
if score < 25:
    max_objects = 5
elif score < 60:
    max_objects = 10
else:
    switch_to_unpredictable_objects()
```

### 🖼️ Sprite Rendering

```python
img = pygame.image.load("assets/car.png").convert_alpha()
img = pygame.transform.scale(img, (40, 40))
screen.blit(img, (x, y))
```

### 💾 High Score Persistence

- Stored in `highscore.txt`
- Automatically updated if the current session beats it

---

## 🔁 Game Loop Flow Diagram

```mermaid
flowchart TD
    A[Start Game] --> B[Load Assets & High Score]
    B --> C[Start Game Loop]
    C --> D[Handle Events (Movement, Quit)]
    D --> E[Update Objects (based on score)]
    E --> F[Detect Collision]
    F --> G{Collision?}
    G -- No --> H[Update Score & Draw Everything]
    G -- Yes --> I[Show Game Over & Save High Score]
    H --> C
    I --> J[Exit]
```

---

## 📸 Screenshots

> *(Insert screenshots of the player dodging different objects here)*

---

## 🌟 Future Enhancements (Ideas)

- Add lives or shields
- Power-ups (slow time, teleport, etc.)
- Sound effects and background music
- Level transitions and animations
- Custom themes (space, jungle, city, etc.)

---

## 📝 License

This project is free for educational and non-commercial use. Attribution appreciated.

---

## 🙋‍♂️ Credits

Developed by: [SURYANATH TRIPATHY]  
Assets from: [Kenney.nl](https://kenney.nl/assets), [OpenGameArt.org](https://opengameart.org/)  
Built with: [Pygame](https://www.pygame.org/)
