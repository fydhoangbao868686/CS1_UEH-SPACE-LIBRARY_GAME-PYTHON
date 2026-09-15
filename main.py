from __future__ import annotations

import json
import math
import os
import sys
import time
import random
from dataclasses import dataclass, field
from typing import Callable, Optional, Tuple, Dict, List

import pygame


# ============================================================
# 1) CONFIG - window / fps / directories
# ============================================================
WINDOW_W, WINDOW_H = 1280, 720
FPS = 60

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
BGM_DIR = os.path.join(ASSETS_DIR, "bgm")
SFX_DIR = os.path.join(ASSETS_DIR, "sfx")

LAYOUT_PATH = os.path.join(BASE_DIR, "ui_layout.json")
INDEX_XLSX_PATH = os.path.join(BASE_DIR, "INDEX.xlsx")
DATASET_XLSX_PATH = os.path.join(BASE_DIR, "Dataset.xlsx")
PRESSSTART_TTF_CANDIDATES = [
    os.path.join(BASE_DIR, "PressStart2P-Regular.ttf"),
]

# ============================================================
# 2) ASSET PATHS 
# ============================================================

# Scene 1 (Title)
SC1_BG_PATH = os.path.join(ASSETS_DIR, "scene1.png")
SC1_PLAY_PATH = os.path.join(ASSETS_DIR, "play_button.png")
SC1_PROJECT_SCENE_PATH = os.path.join(ASSETS_DIR, "project_scene.png")
SC1_GAME_SCENE_PATH    = os.path.join(ASSETS_DIR, "game_scene.png")

SC1_PROJECT_BTN_PATH = os.path.join(ASSETS_DIR, "project_button.png")
SC1_GAME_BTN_PATH    = os.path.join(ASSETS_DIR, "game_button.png")
SC1_OK_BTN_PATH      = os.path.join(ASSETS_DIR, "ok_button.png")

# Scene 2 (ID)
SC2_BG_PATH = os.path.join(ASSETS_DIR, "scene2.png")
SC2_X_PATH = os.path.join(ASSETS_DIR, "x_button.png")
SC2_START_PATH = os.path.join(ASSETS_DIR, "start_button.png")
SC2_INPUTBOX_PATH = os.path.join(ASSETS_DIR, "input_box.png")

# Video cutscenes
SC3_VIDEO_PATH  = os.path.join(ASSETS_DIR, "context1.mp4")
SC4_VIDEO_PATH  = os.path.join(ASSETS_DIR, "context2.mp4")
SC7_VIDEO_PATH  = os.path.join(ASSETS_DIR, "context3.mp4")
SC11_VIDEO_PATH = os.path.join(ASSETS_DIR, "context4.mp4")
SC16_VIDEO_PATH = os.path.join(ASSETS_DIR, "context5.mp4")
SC20_VIDEO_PATH = os.path.join(ASSETS_DIR, "context6.mp4")
SC22_VIDEO_PATH = os.path.join(ASSETS_DIR, "context7.mp4")
SC24_VIDEO_PATH = os.path.join(ASSETS_DIR, "context8.mp4")
SC26_VIDEO_PATH = os.path.join(ASSETS_DIR, "context9.mp4")
SC28_VIDEO_PATH = os.path.join(ASSETS_DIR, "context10.mp4")

# Scene 5 (input)
SC5_BG_PATH = os.path.join(ASSETS_DIR, "scene5.png")
SC5_INPUT_PATH = os.path.join(ASSETS_DIR, "input.png")

# Done screens (6,10,15,19,23,27 share done.png)
SC6_BG_PATH  = os.path.join(ASSETS_DIR, "scene6.png")
SC10_BG_PATH = os.path.join(ASSETS_DIR, "scene10.png")
SC15_BG_PATH = os.path.join(ASSETS_DIR, "scene15.png")
SC19_BG_PATH = os.path.join(ASSETS_DIR, "scene19.png")
SC23_BG_PATH = os.path.join(ASSETS_DIR, "scene23.png")
SC27_BG_PATH = os.path.join(ASSETS_DIR, "scene27.png")
DONE_PATH    = os.path.join(ASSETS_DIR, "done.png")

# Scene 8 (password / forgot)
SC8_BG_PATH = os.path.join(ASSETS_DIR, "scene8.png")
SC8_PASSWORD_PATH = os.path.join(ASSETS_DIR, "password_button.png")
SC8_FORGOT_PATH = os.path.join(ASSETS_DIR, "forgot_button.png")

# Scene 9 (input2)
SC9_BG_PATH = os.path.join(ASSETS_DIR, "scene9.png")
SC9_INPUT_PATH = os.path.join(ASSETS_DIR, "input2.png")

# Scene 12 (laptop click)
SC12_BG_PATH = os.path.join(ASSETS_DIR, "scene12.png")
SC12_LAPTOP_PATH = os.path.join(ASSETS_DIR, "laptop_button.png")

# Scene 13 (dataset)
SC13_BG_PATH = os.path.join(ASSETS_DIR, "scene13.png")
SC13_SCREEN_PATH = os.path.join(ASSETS_DIR, "data_screen.png")
SC13_ARROW_PATH = os.path.join(ASSETS_DIR, "arrow_button.png")
SC13_NEXT_PATH = os.path.join(ASSETS_DIR, "next_button.png")

# Scene 14 (input3)
SC14_BG_PATH = os.path.join(ASSETS_DIR, "scene14.png")
SC14_INPUT_PATH = os.path.join(ASSETS_DIR, "input3.png")

# Scene 17 (next)
SC17_BG_PATH = os.path.join(ASSETS_DIR, "scene17.png")
SC17_NEXT_PATH = os.path.join(ASSETS_DIR, "next_button2.png")

# Scene 18 (input4 + back)
SC18_BG_PATH = os.path.join(ASSETS_DIR, "scene18.png")  
SC18_INPUT_PATH = os.path.join(ASSETS_DIR, "input4.png")
SC18_BACK_PATH = os.path.join(ASSETS_DIR, "back_button.png")

# Scene 21 (input5)
SC21_BG_PATH = os.path.join(ASSETS_DIR, "scene21.png")
SC21_INPUT_PATH = os.path.join(ASSETS_DIR, "input5.png")

# Scene 25 (input6)
SC25_BG_PATH = os.path.join(ASSETS_DIR, "scene25.png")
SC25_INPUT_PATH = os.path.join(ASSETS_DIR, "input6.png")

# Scene 29 (final)
SC29_BG_PATH = os.path.join(ASSETS_DIR, "scene29.png")


# ============================================================
# 3) AUDIO PATHS
# ============================================================
BGM_TITLE_PATH  = os.path.join(BGM_DIR, "Sound_titlescene.mp3")
BGM_INPUT_PATH  = os.path.join(BGM_DIR, "Sound_scene.mp3")

SFX_CLICK_PATH  = os.path.join(SFX_DIR, "Sound_click.wav")
SFX_CORRECT_PATH = os.path.join(SFX_DIR, "Sound_correct.mp3")
SFX_WRONG_PATH   = os.path.join(SFX_DIR, "Sound_wrong.mp3")
SFX_EFFECT_PATH  = os.path.join(SFX_DIR, "Sound_effect.mp3") 

# ============================================================
# 4) UTILITIES: layout / image helpers
# ============================================================

class LayoutStore:
    """
    Đọc ui_layout.json 1 lần khi start game.
    File này lưu anchor + scale_mult đã calibrate từ trước (bạn KHÔNG mất vị trí).
    """
    def __init__(self, path: str):
        self.path = path
        self.data: dict = {}
        self.reload()

    def reload(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except Exception:
            self.data = {}

    def section(self, key: str) -> dict:
        v = self.data.get(key, {})
        return v if isinstance(v, dict) else {}

    def get_anchor(self, section_key: str, field: str, 
                   default_xy: Tuple[float, float]) -> List[float]:
        sec = self.section(section_key) if section_key else self.data
        v = sec.get(field)
        if isinstance(v, (list, tuple)) and len(v) == 2:
            try:
                return [float(v[0]), float(v[1])]
            except Exception:
                pass
        return [float(default_xy[0]), float(default_xy[1])]

    def get_float(self, section_key: str, field: str, 
                  default: float) -> float:
        sec = self.section(section_key) if section_key else self.data
        v = sec.get(field)
        if isinstance(v, (int, float)):
            return float(v)
        return float(default)

    def get_inset4(self, section_key: str, field: str, 
                   default: List[int]) -> List[int]:
        sec = self.section(section_key)
        v = sec.get(field)
        if isinstance(v, list) and len(v) == 4:
            try:
                return [int(v[0]), int(v[1]), int(v[2]), int(v[3])]
            except Exception:
                pass
        return [int(x) for x in default]


def file_exists(path: str) -> bool:
    return bool(path) and os.path.exists(path)


def load_bg(path: str) -> pygame.Surface:
    """Load background image (no alpha) -> convert for speed."""
    return pygame.image.load(path).convert()


def load_img_alpha(path: str) -> pygame.Surface:
    """Load image with alpha."""
    return pygame.image.load(path).convert_alpha()


def trim_by_transparency(surf: pygame.Surface) -> pygame.Surface:
    """Cắt phần canvas trong suốt -> hitbox khớp vật thể."""
    mask = pygame.mask.from_surface(surf)
    rects = mask.get_bounding_rects()
    if not rects:
        return surf
    r = rects[0].copy()
    for rr in rects[1:]:
        r.union_ip(rr)
    out = pygame.Surface((r.w, r.h), pygame.SRCALPHA)
    out.blit(surf, (0, 0), area=r)
    return out


def load_button(path: str, colorkey: Optional[Tuple[int, int, int]] = (0, 0, 0)) -> pygame.Surface:
    if not file_exists(path):
        raise FileNotFoundError(f"Missing file: {path}")

    img = pygame.image.load(path).convert()  # dùng colorkey -> convert()
    if colorkey is not None:
        img.set_colorkey(colorkey)

    alpha = pygame.Surface(img.get_size(), pygame.SRCALPHA)
    alpha.blit(img, (0, 0))
    alpha = trim_by_transparency(alpha)
    return alpha

def brighten_surface(src: pygame.Surface, factor: float = 1.35) -> pygame.Surface:
    s = src.copy()
    overlay = pygame.Surface(s.get_size(), pygame.SRCALPHA)
    add = int(255 * (factor - 1.0) / factor)
    overlay.fill((add, add, add, 0))
    s.blit(overlay, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
    return s

def fit_letterbox(raw: pygame.Surface, w: int, h: int) -> Tuple[pygame.Surface, pygame.Rect, float]:
    iw, ih = raw.get_size()
    s = min(w / iw, h / ih)
    sw, sh = max(1, int(iw * s)), max(1, int(ih * s))
    surf = pygame.transform.smoothscale(raw, (sw, sh))
    rect = surf.get_rect(center=(w // 2, h // 2))
    return surf, rect, s


def anchor_to_point(bg_rect: pygame.Rect, anchor_xy: Tuple[float, float]) -> Tuple[int, int]:
    ax, ay = anchor_xy
    cx = bg_rect.x + int(bg_rect.w * ax)
    cy = bg_rect.y + int(bg_rect.h * ay)
    return cx, cy


def point_in_mask(mask: pygame.mask.Mask, rect: pygame.Rect, pos: Tuple[int, int]) -> bool:
    if not rect.collidepoint(pos):
        return False
    lx, ly = pos[0] - rect.x, pos[1] - rect.y
    try:
        return mask.get_at((lx, ly)) == 1
    except Exception:
        return False


# ============================================================
# 5) FONTS (load 1 lần, dùng lại)
# ============================================================

class Fonts:
    """Cache font để khỏi load lại nhiều lần."""
    def __init__(self):
        self._cache: Dict[Tuple[str, int], pygame.font.Font] = {}
        # Ưu tiên dùng PressStart2P cho toàn bộ chữ trong game (theo yêu cầu).
        # Nếu có nhiều file font khác nhau, lấy cái tồn tại đầu tiên.
        self.ps_path = None
        for p in PRESSSTART_TTF_CANDIDATES:
            if file_exists(p):
                self.ps_path = p
                break

    def fallback(self, size: int) -> pygame.font.Font:
        # Nếu có PressStart2P thì dùng luôn, để mọi text đồng nhất 1 font.
        if self.ps_path:
            return self.pressstart(size)
        key = ("fallback", size)
        if key in self._cache:
            return self._cache[key]
        f = pygame.font.SysFont("consolas", size)
        self._cache[key] = f
        return f

    def pressstart(self, size: int) -> pygame.font.Font:
        if not self.ps_path:
            return self.fallback(size)
        key = ("pressstart", size)
        if key in self._cache:
            return self._cache[key]
        f = pygame.font.Font(self.ps_path, size)
        self._cache[key] = f
        return f


# ============================================================
# 6) AUDIO MANAGER
# ============================================================

class AudioManager:
    """
    - pygame.mixer.music: dùng cho BGM (nhạc nền, 1 track tại 1 thời điểm)
    - pygame.mixer.Sound : dùng cho SFX (hiệu ứng click/correct/wrong)
    """
    def __init__(self):
        self._bgm_key: Optional[str] = None
        self._sfx: Dict[str, pygame.mixer.Sound] = {}

        self._bgm_paths = {
            "title": BGM_TITLE_PATH,
            "input": BGM_INPUT_PATH,
        }
        self._sfx_paths = {
            "click": SFX_CLICK_PATH,
            "correct": SFX_CORRECT_PATH,
            "wrong": SFX_WRONG_PATH,
            "effect": SFX_EFFECT_PATH,
        }

    def _safe_load_sound(self, path: str) -> Optional[pygame.mixer.Sound]:
        if not file_exists(path):
            return None
        try:
            return pygame.mixer.Sound(path)
        except Exception:
            return None

    def set_bgm(self, key: Optional[str]):
        """
        key:
        - "title" / "input"  -> phát BGM tương ứng
        - None               -> stop BGM (dùng cho scene video)
        """
        if key is None:
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
            self._bgm_key = None
            return

        if key == self._bgm_key:
            return  # đang phát đúng track rồi -> không restart

        path = self._bgm_paths.get(key)
        if not path or not file_exists(path) or not pygame.mixer.get_init():
            self._bgm_key = key
            return

        try:
            pygame.mixer.music.load(path)
            pygame.mixer.music.set_volume(0.65)
            pygame.mixer.music.play(-1)
            self._bgm_key = key
        except Exception:
            self._bgm_key = key

    def sfx(self, key: str):
        """Play SFX (nếu file tồn tại và mixer hoạt động)."""
        if not pygame.mixer.get_init():
            return
        if key not in self._sfx:
            snd = self._safe_load_sound(self._sfx_paths.get(key, ""))
            if snd is None:
                self._sfx[key] = None  # cache miss
            else:
                snd.set_volume(0.75 if key == "click" else 0.9)
                self._sfx[key] = snd
        snd = self._sfx.get(key)
        if snd:
            try:
                snd.play()
            except Exception:
                pass


# ============================================================
# 7) UI COMPONENT: ImageButton (tự quản hover/pressed + click sound)
# ============================================================

@dataclass
class ImageButton:
    """
    Button ảnh:
    - Hover: brighten
    - Click: chỉ tính là "click thật" nếu DOWN trên button và UP vẫn trên button
    - Optional pixel-perfect mask (nếu muốn hitbox khớp hình)
    """
    raw: pygame.Surface
    anchor: Tuple[float, float]
    scale_mult: float = 1.0
    use_mask: bool = False
    smooth: bool = False

    img: Optional[pygame.Surface] = None
    img_hover: Optional[pygame.Surface] = None
    rect: pygame.Rect = field(default_factory=lambda: pygame.Rect(0, 0, 0, 0))
    mask: Optional[pygame.mask.Mask] = None

    hovered: bool = False
    pressed: bool = False

    def rebuild(self, bg_rect: pygame.Rect, bg_scale: float):
        s = bg_scale * self.scale_mult
        w = max(1, int(self.raw.get_width() * s))
        h = max(1, int(self.raw.get_height() * s))

        if self.smooth:
            self.img = pygame.transform.smoothscale(self.raw, (w, h))
        else:
            self.img = pygame.transform.scale(self.raw, (w, h))

        self.img_hover = brighten_surface(self.img, 1.25)
        self.rect = self.img.get_rect(center=anchor_to_point(bg_rect, self.anchor))
        self.mask = pygame.mask.from_surface(self.img) if self.use_mask else None

    def _hit(self, pos: Tuple[int, int]) -> bool:
        if self.mask is None:
            return self.rect.collidepoint(pos)
        return point_in_mask(self.mask, self.rect, pos)

    def update_hover(self, mouse_pos: Tuple[int, int]):
        self.hovered = self._hit(mouse_pos)

    def handle_event(self, event: pygame.event.Event) -> bool:
        """Return True nếu click thành công (UP sau DOWN vẫn nằm trên button)."""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self._hit(event.pos):
                self.pressed = True
                return False
            self.pressed = False

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.pressed:
                self.pressed = False
                if self._hit(event.pos):
                    return True
        return False

    def draw(self, screen: pygame.Surface):
        if not self.img:
            return

        surf = self.img_hover if self.hovered else self.img

        if self.hovered:
            # Giống main.py: hover thì phóng to nhẹ; nếu đang nhấn (pressed) thì thu nhỏ để tạo feedback
            scale = 1.06 if not self.pressed else 0.98
            s = pygame.transform.scale(surf, (int(surf.get_width() * scale), int(surf.get_height() * scale)))
            screen.blit(s, s.get_rect(center=self.rect.center))
        else:
            screen.blit(surf, self.rect.topleft)

# ============================================================
# 8) SCENE SYSTEM (base + manager)
# ============================================================

class Scene:
    """Interface cho Scene."""
    BGM_KEY: Optional[str] = None  # None => stop; "title"/"input" => phát

    def __init__(self, mgr: "SceneManager"):
        self.mgr = mgr

    # hooks (optional)
    def on_enter(self): ...
    def on_exit(self): ...

    def handle_event(self, event: pygame.event.Event): ...
    def update(self, dt: float): ...
    def draw(self, screen: pygame.Surface): ...


class SceneManager:
    """
    Quản lý scene hiện tại + history (để quay lại bằng phím `).
    Lưu ý: history lưu "factory" để tạo scene mới, tránh việc scene cũ giữ tài nguyên (video player).
    """
    def __init__(self, fonts: Fonts, layout: LayoutStore, audio: AudioManager):
        self.fonts = fonts
        self.layout = layout
        self.audio = audio

        self.scene: Optional[Scene] = None
        self.history: List[Callable[[], Scene]] = []

        # Shared game state
        self.player_id: Optional[str] = None
        self.player_name: Optional[str] = None

    def go_to(self, scene: Scene, record_history: bool = True):
        if self.scene is not None:
            # cleanup tài nguyên của scene cũ
            try:
                self.scene.on_exit()
            except Exception:
                pass

            # lưu history để quay lại (debug key `)
            if record_history:
                prev_cls = type(self.scene)
                self.history.append(lambda cls=prev_cls: cls(self))

        self.scene = scene

        # apply BGM policy
        bgm_key = getattr(scene, "BGM_KEY", None)
        self.audio.set_bgm(bgm_key)

        try:
            scene.on_enter()
        except Exception:
            pass

    def back(self):
        if not self.history:
            return
        # exit current
        if self.scene is not None:
            try:
                self.scene.on_exit()
            except Exception:
                pass

        factory = self.history.pop()
        scene = factory()
        self.scene = scene
        self.audio.set_bgm(getattr(scene, "BGM_KEY", None))
        try:
            scene.on_enter()
        except Exception:
            pass


# ============================================================
# 9) GENERIC SCENES (video / input / done / click-object)
# ============================================================

class VideoCutscene(Scene):
    """
    Generic video cutscene:
    - Phát video mp4 có audio bằng ffpyplayer
    - Sync bằng PTS để giảm lệch tiếng/ảnh
    - SPACE / ENTER / Left click: skip -> next scene
    - LOOP option: video lặp vô hạn (vẫn cho skip)
    """
    BGM_KEY = None  # stop bgm

    def __init__(self, mgr: SceneManager, video_path: str, next_scene_factory: Callable[[SceneManager], Scene], loop: bool = False):
        super().__init__(mgr)
        self.video_path = video_path
        self.next_scene_factory = next_scene_factory
        self.loop = loop

        self.player = None
        self.err = ""
        self.finished = False

        self.last_frame_surf: Optional[pygame.Surface] = None
        self.pending_frame = None  # (img, pts)

        self.start_ts = time.perf_counter()
        self.sync_tolerance = 0.020

        try:
            from ffpyplayer.player import MediaPlayer  # type: ignore
        except Exception as e:
            self.err = f"Missing ffpyplayer. Install: pip install ffpyplayer ({e})"
            return

        if not file_exists(self.video_path):
            self.err = f"Missing video file: {self.video_path}"
            return

        self._MediaPlayer = MediaPlayer
        self._open_player()

    def _open_player(self):
        # ffpyplayer phát audio tự động; sync audio để ổn định
        self.player = self._MediaPlayer(self.video_path, ff_opts={"sync": "audio"})
        self.start_ts = time.perf_counter()
        self.pending_frame = None
        self.finished = False

    def _elapsed(self) -> float:
        return time.perf_counter() - self.start_ts

    def on_exit(self):
        self._close()

    def _close(self):
        try:
            if self.player:
                self.player.close_player()
        except Exception:
            pass
        self.player = None

    def _go_next(self):
        self._close()
        self.mgr.go_to(self.next_scene_factory(self.mgr))

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                self._go_next()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._go_next()

    def update(self, dt: float):
        if self.player is None:
            return

        now = self._elapsed()

        # pending frame (pts tương lai)
        if self.pending_frame is not None:
            img, pts = self.pending_frame
            if pts <= now + self.sync_tolerance:
                self.last_frame_surf = self._img_to_surface(img)
                self.pending_frame = None
            else:
                return

        for _ in range(3):
            frame, val = self.player.get_frame()

            if val == "eof":
                if self.loop:
                    # lặp: reopen player từ đầu
                    self._close()
                    self._open_player()
                    return
                self.finished = True
                return

            if frame is None:
                return

            img, _t = frame
            pts = float(val) if isinstance(val, (int, float)) else None

            if pts is None:
                self.last_frame_surf = self._img_to_surface(img)
                return

            if pts > now + self.sync_tolerance:
                self.pending_frame = (img, pts)
                return

            self.last_frame_surf = self._img_to_surface(img)

    def _img_to_surface(self, img):
        w, h = img.get_size()
        data = img.to_bytearray()[0]
        return pygame.image.frombuffer(data, (w, h), "RGB")

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))

        if self.player is None:
            t = self.mgr.fonts.fallback(22).render(self.err, True, (255, 255, 255))
            screen.blit(t, (20, 20))
            return

        if self.last_frame_surf is None:
            return #màn hình đen
        else:
            vw, vh = self.last_frame_surf.get_size()
            s = min(WINDOW_W / vw, WINDOW_H / vh)
            dw, dh = int(vw * s), int(vh * s)
            img = pygame.transform.smoothscale(self.last_frame_surf, (dw, dh))
            x = (WINDOW_W - dw) // 2
            y = (WINDOW_H - dh) // 2
            screen.blit(img, (x, y))

        if self.finished or self.loop:
            hint = self.mgr.fonts.fallback(14).render("Click/ Enter/ Space to continue", True, (255, 255, 255))
            screen.blit(hint, (WINDOW_W // 2 - hint.get_width() // 2, WINDOW_H - 80))

class VideoCutsceneNoBgm(VideoCutscene):
    BGM_KEY = None
    def on_enter(self):
        self.mgr.audio.set_bgm(None)


class DonePopupScene(Scene):
    """
    Scene dạng "DONE" (popup):
    - Hiệu ứng popup + fade (giữ gần như y hệt bản cũ để bạn không bị "mất cảm giác" gameplay)
    - Sau khi animation xong: SPACE/ENTER/Click để qua scene tiếp
    """
    BGM_KEY = None

    DEFAULT_DONE_ANCHOR = (0.50, 0.53)
    DEFAULT_DONE_SCALE = 1.0

    # Tổng thời gian animation (giống code cũ)
    POPUP_DURATION_SEC = 2.2

    def __init__(self, mgr: SceneManager, bg_path: str, layout_key: str, next_scene_factory: Callable[[SceneManager], Scene]):
        super().__init__(mgr)
        self.bg_path = bg_path
        self.layout_key = layout_key
        self.next_scene_factory = next_scene_factory

        self.missing_assets: List[str] = []
        for p in (bg_path, DONE_PATH):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))

        self.bg_raw = None
        self.bg = None
        self.bg_pos = (0, 0)
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_scale = 1.0

        self.done_raw = None
        self.done_img = None  # bản scale theo layout (chưa animation)
        self.done_rect = pygame.Rect(0, 0, 0, 0)

        # layout
        self.done_anchor = tuple(self.mgr.layout.get_anchor(layout_key, "done_anchor", self.DEFAULT_DONE_ANCHOR))
        self.done_scale_mult = self.mgr.layout.get_float(layout_key, "done_scale_mult", self.DEFAULT_DONE_SCALE)

        # animation state
        self.elapsed = 0.0
        self.ready = False

        if not self.missing_assets:
            self._load_assets()
            self._rebuild()

    def _load_assets(self):
        self.bg_raw = load_bg(self.bg_path)
        self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
        self.bg_pos = self.bg_rect.topleft
        self.done_raw = load_img_alpha(DONE_PATH)

    @staticmethod
    def _ease_out_back(x: float) -> float:
        c1 = 1.70158
        c3 = c1 + 1
        return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2

    def _rebuild(self):
        if self.done_raw is None:
            return
        s = self.bg_scale * self.done_scale_mult
        w = max(1, int(self.done_raw.get_width() * s))
        h = max(1, int(self.done_raw.get_height() * s))
        self.done_img = pygame.transform.smoothscale(self.done_raw, (w, h))
        self.done_rect = self.done_img.get_rect(center=anchor_to_point(self.bg_rect, self.done_anchor))

    def _go_next(self):
        self.mgr.go_to(self.next_scene_factory(self.mgr))

    def handle_event(self, event: pygame.event.Event):
        if not self.ready:
            return
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
            self._go_next()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._go_next()

    def update(self, dt: float):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        if self.missing_assets:
            return
        self.elapsed += dt
        if self.elapsed >= self.POPUP_DURATION_SEC:
            self.ready = True

    def _anim_scale_alpha(self) -> Tuple[float, int]:
        """
        Trả về (scale, alpha) theo timeline:
        - 0%..35%: popup (scale tăng nhanh + overshoot nhẹ)
        - Sau đó: giữ nguyên (KHÔNG fade out nữa)
        """
       
        x = max(0.0, min(1.0, self.elapsed / self.POPUP_DURATION_SEC))

        if x < 0.35:
            u = x / 0.35
            s = 0.60 + 0.40 * self._ease_out_back(u)
            a = int(255 * min(1.0, u / 0.60))
            return s, max(0, min(255, a))

        # Sau khi popup xong: giữ nguyên 100% size và alpha 255 mãi mãi
        return 1.0, 255


    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))
        if self.missing_assets or self.bg is None or self.done_img is None:
            t = self.mgr.fonts.fallback(22).render("DONE scene missing assets:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return

        screen.blit(self.bg, self.bg_pos)

        scale, alpha = self._anim_scale_alpha()
        if alpha <= 0:
            return

        w = max(1, int(self.done_img.get_width() * scale))
        h = max(1, int(self.done_img.get_height() * scale))
        img = pygame.transform.smoothscale(self.done_img, (w, h))
        img.set_alpha(alpha)
        r = img.get_rect(center=self.done_rect.center)
        screen.blit(img, r.topleft)


class TextAnswerScene(Scene):
    """
    Scene nhập liệu 1 dòng:
    - Hiển thị background + input bar
    - Người chơi gõ đáp án -> Enter để submit
    - Đúng: play SFX correct + chuyển scene
    - Sai : play SFX wrong + overlay đen, bấm SPACE/ENTER/click để thử lại
    """
    BGM_KEY = "input"

    DEFAULT_INPUT_ANCHOR = (0.50, 0.58)
    DEFAULT_INPUT_SCALE = 1.0

    def __init__(
        self,
        mgr: SceneManager,
        bg_path: str,
        input_path: str,
        layout_key: str,
        answer_check: Callable[[str], bool],
        next_scene_factory: Callable[[SceneManager], Scene],
        wrong_text: str = "Wrong answer. Try again!",
        max_len: int = 80,
        char_filter: Optional[Callable[[str], bool]] = None,
        back_button: Optional[Tuple[str, str, Tuple[float, float], float, Callable[[SceneManager], Scene]]] = None,
    ):
        super().__init__(mgr)
        self.bg_path = bg_path
        self.input_path = input_path
        self.layout_key = layout_key
        self.answer_check = answer_check
        self.next_scene_factory = next_scene_factory
        self.wrong_text = wrong_text
        self.max_len = max_len
        self.char_filter = char_filter or (lambda ch: ch.isprintable() and ch not in "\t\r\n")

        # optional back button: (path, layout_field_prefix, default_anchor, default_scale, target_scene_factory)
        self.back_spec = back_button

        self.mode = "form"  # "form" | "error"

        self.input_text = ""
        self.focus_input = True
        self.caret_timer = 0.0
        self.caret_on = True

        self.missing_assets: List[str] = []
        for p in (bg_path, input_path):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))
        if self.back_spec:
            bp = self.back_spec[0]
            if not file_exists(bp):
                self.missing_assets.append(os.path.basename(bp))

        self.bg_raw = None
        self.bg = None
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_pos = (0, 0)
        self.bg_scale = 1.0

        self.input_raw = None
        self.input_img = None
        self.input_rect = pygame.Rect(0, 0, 0, 0)

        self.back_btn: Optional[ImageButton] = None
        self._load_assets()
        self._load_layout_and_build()

    def _load_assets(self):
        if self.missing_assets:
            return
        self.bg_raw = load_bg(self.bg_path)
        self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
        self.bg_pos = self.bg_rect.topleft

        self.input_raw = load_button(self.input_path, colorkey=(0, 0, 0))

        if self.back_spec:
            back_path, _prefix, _d_anchor, _d_scale, _target = self.back_spec
            back_raw = load_button(back_path, colorkey=(0, 0, 0))
            # placeholder, anchor/scale load later
            self.back_btn = ImageButton(back_raw, anchor=(0.1, 0.1), scale_mult=1.0, use_mask=True, smooth=False)

    def _load_layout_and_build(self):
        if self.missing_assets:
            return

        input_anchor = tuple(self.mgr.layout.get_anchor(self.layout_key, "input_anchor", self.DEFAULT_INPUT_ANCHOR))
        input_scale_mult = self.mgr.layout.get_float(self.layout_key, "input_scale_mult", self.DEFAULT_INPUT_SCALE)

        # build input
        s = self.bg_scale * input_scale_mult
        w = max(1, int(self.input_raw.get_width() * s))
        h = max(1, int(self.input_raw.get_height() * s))
        self.input_img = pygame.transform.scale(self.input_raw, (w, h))
        self.input_rect = self.input_img.get_rect(center=anchor_to_point(self.bg_rect, input_anchor))

        # build back button if any
        if self.back_spec and self.back_btn:
            back_path, prefix, d_anchor, d_scale, _target = self.back_spec
            a = tuple(self.mgr.layout.get_anchor(self.layout_key, f"{prefix}_anchor", d_anchor))
            sm = self.mgr.layout.get_float(self.layout_key, f"{prefix}_scale_mult", d_scale)
            self.back_btn.anchor = a
            self.back_btn.scale_mult = sm
            self.back_btn.rebuild(self.bg_rect, self.bg_scale)

    def _submit(self):
        ans = self.input_text.strip()
        if self.answer_check(ans):
            self.mgr.audio.sfx("correct")
            self.mgr.go_to(self.next_scene_factory(self.mgr))
        else:
            self.mgr.audio.sfx("wrong")
            self.mode = "error"
            self.focus_input = False

    def _back_to_form(self):
        self.mode = "form"
        self.input_text = ""
        self.focus_input = True

    def handle_event(self, event: pygame.event.Event):
        if self.missing_assets:
            return

        # ERROR overlay
        if self.mode == "error":
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                self._back_to_form()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._back_to_form()
            return

        # optional back button click (chỉ mouse)
        if self.back_btn and self.back_spec:
            if self.back_btn.handle_event(event):
                self.mgr.audio.sfx("click")
                target_factory = self.back_spec[4]
                self.mgr.go_to(target_factory(self.mgr))
                return

        # FORM
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self._submit()
                return

            if not self.focus_input:
                return

            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
                return

            ch = event.unicode
            if ch and self.char_filter(ch):
                if len(self.input_text) < self.max_len:
                    self.input_text += ch

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # click focus input (KHÔNG phát click sfx vì đây không phải button)
            if self.input_rect.collidepoint(event.pos):
                self.focus_input = True
            else:
                self.focus_input = False

    def update(self, dt: float):
        # caret blink
        self.caret_timer += dt
        if self.caret_timer >= 0.45:
            self.caret_timer = 0.0
            self.caret_on = not self.caret_on

        if self.missing_assets:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        if self.mode != "form":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        mp = pygame.mouse.get_pos()

        if self.back_btn:
            self.back_btn.update_hover(mp)

        if self.input_rect.collidepoint(mp):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        else:
            # nếu hover back_btn thì hand
            if self.back_btn and self.back_btn.hovered:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen: pygame.Surface):
        if self.missing_assets:
            screen.fill((10, 10, 10))
            t = self.mgr.fonts.fallback(22).render("Input scene missing assets:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return

        screen.fill((0, 0, 0))
        screen.blit(self.bg, self.bg_pos)

        # draw back button
        if self.back_btn:
            self.back_btn.draw(screen)

        # draw input bar
        screen.blit(self.input_img, self.input_rect.topleft)

        # draw text inside input (GIỐNG main.py)
        # Lưu ý: nhiều màn input của bạn dùng inflate(-80, -30) để chữ nằm đúng giữa ô
        f_main = self.mgr.fonts.pressstart(18)
        inner = self.input_rect.inflate(-80, -30)

        txt_show = self.input_text + ("|" if (self.mode == "form" and self.focus_input and self.caret_on) else "")
        surf = f_main.render(txt_show, True, (20, 20, 20))
        if surf.get_width() > inner.w:
            tail = txt_show[-30:]
            surf = f_main.render(tail, True, (20, 20, 20))

        screen.blit(surf, (inner.x + 10, inner.y + inner.h // 2 - surf.get_height() // 2))

        # error overlay
        if self.mode == "error":
            overlay = pygame.Surface((WINDOW_W, WINDOW_H))
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            f = self.mgr.fonts.pressstart(18)
            msg = f.render(self.wrong_text, True, (255, 255, 255))
            screen.blit(msg, (WINDOW_W // 2 - msg.get_width() // 2, WINDOW_H // 2 - msg.get_height() // 2))

            hint = self.mgr.fonts.pressstart(14).render("You can do it! Click / Enter / Space to try again", True, (255, 255, 255))
            screen.blit(hint, (WINDOW_W // 2 - hint.get_width() // 2, WINDOW_H // 2 + 60))


class ClickObjectScene(Scene):
    """
    Scene click 1 object để qua màn:
    - ví dụ Scene12 (click laptop), Scene17 (click next)
    - Click đúng object -> play click SFX -> qua scene tiếp
    """
    BGM_KEY = "input"

    def __init__(
        self,
        mgr: SceneManager,
        bg_path: str,
        obj_path: str,
        layout_key: str,
        anchor_field: str,
        scale_field: str,
        default_anchor: Tuple[float, float],
        default_scale: float,
        next_scene_factory: Callable[[SceneManager], Scene],
        use_mask: bool = True,
        allow_keys: bool = False,
        obj_colorkey: Optional[Tuple[int, int, int]] = (0, 0, 0),
    ):
        super().__init__(mgr)
        self.bg_path = bg_path
        self.obj_path = obj_path
        self.layout_key = layout_key
        self.anchor_field = anchor_field
        self.scale_field = scale_field
        self.default_anchor = default_anchor
        self.default_scale = default_scale
        self.next_scene_factory = next_scene_factory
        self.use_mask = use_mask
        self.allow_keys = allow_keys
        self.obj_colorkey = obj_colorkey

        self.missing_assets: List[str] = []
        for p in (bg_path, obj_path):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))

        self.bg_raw = None
        self.bg = None
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_pos = (0, 0)
        self.bg_scale = 1.0

        self.button: Optional[ImageButton] = None

        if not self.missing_assets:
            self._load_assets()
            self._build_button()

    def _load_assets(self):
        self.bg_raw = load_bg(self.bg_path)
        self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
        self.bg_pos = self.bg_rect.topleft

        if self.obj_colorkey is None:
            # Dành cho asset đã có alpha thật (ví dụ laptop.png), tránh set colorkey làm mất chi tiết đen.
            raw = trim_by_transparency(load_img_alpha(self.obj_path))
        else:
            raw = load_button(self.obj_path, colorkey=self.obj_colorkey)
        a = tuple(self.mgr.layout.get_anchor(self.layout_key, self.anchor_field, self.default_anchor))
        sm = self.mgr.layout.get_float(self.layout_key, self.scale_field, self.default_scale)
        self.button = ImageButton(raw, anchor=a, scale_mult=sm, use_mask=self.use_mask, smooth=False)

    def _build_button(self):
        if self.button:
            self.button.rebuild(self.bg_rect, self.bg_scale)

    def _go_next(self):
        self.mgr.go_to(self.next_scene_factory(self.mgr))

    def handle_event(self, event: pygame.event.Event):
        if self.missing_assets:
            return

        if self.allow_keys and event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
            self._go_next()
            return

        if self.button and self.button.handle_event(event):
            self.mgr.audio.sfx("click")
            self._go_next()

    def update(self, dt: float):
        if self.missing_assets:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return
        mp = pygame.mouse.get_pos()
        if self.button:
            self.button.update_hover(mp)
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if self.button.hovered else pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))
        if self.missing_assets or self.bg is None:
            t = self.mgr.fonts.fallback(22).render("Scene missing assets:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return
        screen.blit(self.bg, self.bg_pos)
        if self.button:
            self.button.draw(screen)
class BlackTextTransitionScene(Scene):
    """
    Màn hình đen + text xuất hiện ngay
    - Chặn input 0.5s
    - Phát Sound_effect.mp3 (key: "effect")
    - Chỉ cho qua tiếp khi sound kết thúc AND đã qua 0.5s
    """
    BGM_KEY = None  # stop bgm để không chồng tiếng

    def __init__(self, mgr: SceneManager, text: str, next_scene_factory: Callable[[SceneManager], Scene], min_lock: float = 0.5):
        super().__init__(mgr)
        self.text = text
        self.next_scene_factory = next_scene_factory
        self.min_lock = min_lock

        self.elapsed = 0.0
        self.ready = False

        self._channel: Optional[pygame.mixer.Channel] = None

    def on_enter(self):
        # phát effect sound ngay khi vào scene
        if pygame.mixer.get_init():
            snd = self.mgr.audio._safe_load_sound(SFX_EFFECT_PATH)  # reuse helper (private but ok)
            if snd:
                snd.set_volume(0.9)
                self._channel = snd.play()
            else:
                self._channel = None

    def _sound_done(self) -> bool:
        # Nếu không có audio device hoặc load fail -> coi như đã xong
        if self._channel is None:
            return True
        try:
            return not self._channel.get_busy()
        except Exception:
            return True

    def update(self, dt: float):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        self.elapsed += dt
        if (self.elapsed >= self.min_lock) and self._sound_done():
            self.ready = True

    def handle_event(self, event: pygame.event.Event):
        if not self.ready:
            return
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.mgr.go_to(self.next_scene_factory(self.mgr))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.mgr.go_to(self.next_scene_factory(self.mgr))

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))
        f = self.mgr.fonts.pressstart(22)
        msg = f.render(self.text, True, (255, 255, 255))
        screen.blit(msg, (WINDOW_W // 2 - msg.get_width() // 2, WINDOW_H // 2 - msg.get_height() // 2))

        if self.ready:
            hint = self.mgr.fonts.pressstart(14).render("Click / Space / Enter to continue", True, (255, 255, 255))
            screen.blit(hint, (WINDOW_W // 2 - hint.get_width() // 2, WINDOW_H // 2 + 60))


# ============================================================
# 10) SCENES (1..29)
# ============================================================

# NOTE - Scene flow (để bạn dễ giải thích với thầy):
#   1(Title) -> 2(ID) -> 3(Video) -> 4(Video loop) -> 5(Input) -> 6(DONE) -> 7(Video) -> 8(Password) -> 9(Input) -> 10(DONE)
#   -> 11(Video) -> 12(Click object) -> 13(Dataset) -> 14(Input) -> 15(DONE) -> 16(Video) -> 17(Next) -> 18(Input) -> 19(DONE)
#   -> 20(Video) -> 21(Input) -> 22(Video) -> 23(DONE) -> 24(Video) -> 25(Input) -> 26(Video) -> 27(DONE) -> 28(Video) -> 29(Final) -> 1(Title)
#
# NOTE - Điều khiển chung (global, viết ở MAIN LOOP):
#   ESC  : về TitleScene (trừ khi đang ở TitleScene).
#   `    : quay lại scene trước (debug/test).


class TitleScene(Scene):
    """
    Scene 1: Title (HOME)
    - HOME: PLAY / PROJECT / GAME
    - PROJECT page: project_scene.png + OK (về HOME)
    - GAME page:    game_scene.png    + OK (về HOME)
    - Calibration: F2 (tách riêng - có thể xóa sau)
    """
    BGM_KEY = "title"

    DEFAULT_PLAY_ANCHOR = (0.50, 0.75)
    DEFAULT_PLAY_SCALE  = 1.0

    # NEW defaults
    DEFAULT_PROJECT_ANCHOR = (0.08, 0.12)
    DEFAULT_GAME_ANCHOR    = (0.90, 0.12)
    DEFAULT_OK_ANCHOR      = (0.92, 0.86)

    DEFAULT_PROJECT_SCALE = 1.0
    DEFAULT_GAME_SCALE    = 1.0
    DEFAULT_OK_SCALE      = 1.0

    def __init__(self, mgr: SceneManager):
        super().__init__(mgr)

        self.show_quit_confirm = False

        # NEW: internal page state (không tạo Scene mới)
        self.page = "home"  # "home" | "project" | "game"

        self.missing_assets: List[str] = []
        for p in (
            SC1_BG_PATH, SC1_PLAY_PATH,
            SC1_PROJECT_BTN_PATH, SC1_GAME_BTN_PATH,
            SC1_PROJECT_SCENE_PATH, SC1_GAME_SCENE_PATH,
            SC1_OK_BTN_PATH,
        ):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))

        # backgrounds
        self.bg_raw = None
        self.bg = None
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_pos = (0, 0)
        self.bg_scale = 1.0

        # NEW: subpage backgrounds (scaled like main bg)
        self.project_bg = None
        self.game_bg = None

        # buttons
        self.play_btn: Optional[ImageButton] = None
        self.project_btn: Optional[ImageButton] = None
        self.game_btn: Optional[ImageButton] = None
        self.ok_btn: Optional[ImageButton] = None

        if not self.missing_assets:
            self._load_assets()
            self._load_layout_buttons()
            self._rebuild_buttons()

    def _load_assets(self):
        # base bg
        self.bg_raw = load_bg(SC1_BG_PATH)
        self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
        self.bg_pos = self.bg_rect.topleft

        # subpage backgrounds (fit same way for consistency)
        proj_raw = load_bg(SC1_PROJECT_SCENE_PATH)
        game_raw = load_bg(SC1_GAME_SCENE_PATH)
        self.project_bg, _r1, _s1 = fit_letterbox(proj_raw, WINDOW_W, WINDOW_H)
        self.game_bg, _r2, _s2 = fit_letterbox(game_raw, WINDOW_W, WINDOW_H)

        # button raw
        play_raw = load_button(SC1_PLAY_PATH, colorkey=(0, 0, 0))
        project_raw = load_button(SC1_PROJECT_BTN_PATH, colorkey=(0, 0, 0))
        game_raw_btn = load_button(SC1_GAME_BTN_PATH, colorkey=(0, 0, 0))
        ok_raw = load_button(SC1_OK_BTN_PATH, colorkey=(0, 0, 0))

        # create buttons (anchor/scale set later)
        self.play_btn = ImageButton(play_raw, anchor=(0.5, 0.5), scale_mult=1.0, use_mask=False, smooth=False)
        self.project_btn = ImageButton(project_raw, anchor=(0.5, 0.5), scale_mult=1.0, use_mask=True, smooth=False)
        self.game_btn = ImageButton(game_raw_btn, anchor=(0.5, 0.5), scale_mult=1.0, use_mask=True, smooth=False)
        self.ok_btn = ImageButton(ok_raw, anchor=(0.5, 0.5), scale_mult=1.0, use_mask=True, smooth=False)

    def _load_layout_buttons(self):
        # TitleScene dùng root keys (""), đúng style của bạn
        a_play = tuple(self.mgr.layout.get_anchor("", "play_anchor", self.DEFAULT_PLAY_ANCHOR))
        s_play = self.mgr.layout.get_float("", "play_scale_mult", self.DEFAULT_PLAY_SCALE)

        a_proj = tuple(self.mgr.layout.get_anchor("", "project_anchor", self.DEFAULT_PROJECT_ANCHOR))
        s_proj = self.mgr.layout.get_float("", "project_scale_mult", self.DEFAULT_PROJECT_SCALE)

        a_game = tuple(self.mgr.layout.get_anchor("", "game_anchor", self.DEFAULT_GAME_ANCHOR))
        s_game = self.mgr.layout.get_float("", "game_scale_mult", self.DEFAULT_GAME_SCALE)

        a_ok = tuple(self.mgr.layout.get_anchor("", "ok_anchor", self.DEFAULT_OK_ANCHOR))
        s_ok = self.mgr.layout.get_float("", "ok_scale_mult", self.DEFAULT_OK_SCALE)

        self.play_btn.anchor, self.play_btn.scale_mult = a_play, s_play
        self.project_btn.anchor, self.project_btn.scale_mult = a_proj, s_proj
        self.game_btn.anchor, self.game_btn.scale_mult = a_game, s_game
        self.ok_btn.anchor, self.ok_btn.scale_mult = a_ok, s_ok

    def _rebuild_buttons(self):
        # rebuild theo bg_rect/bg_scale
        if self.play_btn: self.play_btn.rebuild(self.bg_rect, self.bg_scale)
        if self.project_btn: self.project_btn.rebuild(self.bg_rect, self.bg_scale)
        if self.game_btn: self.game_btn.rebuild(self.bg_rect, self.bg_scale)
        if self.ok_btn: self.ok_btn.rebuild(self.bg_rect, self.bg_scale)

    # -------- transitions inside TitleScene --------
    def _go_play(self, by_mouse: bool):
        if by_mouse:
            self.mgr.audio.sfx("click")
        self.mgr.go_to(Scene2(self.mgr))

    def _open_project(self):
        self.mgr.audio.sfx("click")
        self.page = "project"

    def _open_game(self):
        self.mgr.audio.sfx("click")
        self.page = "game"

    def _back_home(self):
        self.mgr.audio.sfx("click")
        self.page = "home"

    def handle_event(self, event: pygame.event.Event):

        # quit confirm mode (giữ như cũ)
        if self.show_quit_confirm:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    pygame.quit()
                    sys.exit()
                if event.key in (pygame.K_n, pygame.K_ESCAPE):
                    self.show_quit_confirm = False
            return

        # HOME page
        if self.page == "home":
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    self._go_play(by_mouse=False)
                elif event.key == pygame.K_ESCAPE:
                    self.show_quit_confirm = True

            # mouse clicks (play/project/game)
            if self.play_btn and self.play_btn.handle_event(event):
                self._go_play(by_mouse=True)

            if self.project_btn and self.project_btn.handle_event(event):
                self._open_project()

            if self.game_btn and self.game_btn.handle_event(event):
                self._open_game()

            return

        # PROJECT / GAME page: chỉ OK để quay lại HOME (giống play_button behavior)
        if self.page in ("project", "game"):
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_ESCAPE,):
                # ESC quay về HOME nhanh (tuỳ bạn giữ/ bỏ)
                self.page = "home"
                return

            if self.ok_btn and self.ok_btn.handle_event(event):
                self._back_home()
            return

    def update(self, dt: float):
        if self.missing_assets:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        if self.show_quit_confirm:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        mp = pygame.mouse.get_pos()

        # hover cursor theo page
        if self.page == "home":
            hover_any = False
            for b in (self.play_btn, self.project_btn, self.game_btn):
                if b:
                    b.update_hover(mp)
                    hover_any |= b.hovered
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if hover_any else pygame.SYSTEM_CURSOR_ARROW)
        else:
            if self.ok_btn:
                self.ok_btn.update_hover(mp)
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if self.ok_btn.hovered else pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))

        if self.missing_assets or self.bg is None:
            t = self.mgr.fonts.fallback(22).render("Title assets missing:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return

        # background by page
        if self.page == "home":
            screen.blit(self.bg, self.bg_pos)
            if self.play_btn: self.play_btn.draw(screen)
            if self.project_btn: self.project_btn.draw(screen)
            if self.game_btn: self.game_btn.draw(screen)
        elif self.page == "project":
            screen.blit(self.project_bg, self.bg_pos)
            if self.ok_btn: self.ok_btn.draw(screen)
        elif self.page == "game":
            screen.blit(self.game_bg, self.bg_pos)
            if self.ok_btn: self.ok_btn.draw(screen)

        # quit confirm overlay (giữ như cũ)
        if self.show_quit_confirm:
            overlay = pygame.Surface((WINDOW_W, WINDOW_H), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 160))
            screen.blit(overlay, (0, 0))

            box = pygame.Rect(0, 0, 520, 180)
            box.center = (WINDOW_W // 2, WINDOW_H // 2)
            pygame.draw.rect(screen, (235, 235, 235), box, border_radius=10)
            pygame.draw.rect(screen, (30, 30, 30), box, 4, border_radius=10)

            t = self.mgr.fonts.fallback(28).render("Thoát game? (Y/N)", True, (10, 10, 10))
            t2 = self.mgr.fonts.fallback(22).render("Y: Quit   N: Cancel", True, (10, 10, 10))
            screen.blit(t, (box.centerx - t.get_width() // 2, box.y + 55))
            screen.blit(t2, (box.centerx - t2.get_width() // 2, box.y + 100))


class Scene2(Scene):
    """
    Scene 2: Nhập ID người chơi (đọc từ INDEX.xlsx)
    - Đúng ID: overlay typewriter "Hello <Name>" -> SPACE/ENTER/click -> Scene3
    - Sai ID : overlay typewriter "Sorry..."       -> SPACE/ENTER/click -> nhập lại
    """
    BGM_KEY = "title"

    DEFAULT_X_ANCHOR = (0.27, 0.26)
    DEFAULT_BOX_ANCHOR = (0.50, 0.55)
    DEFAULT_START_ANCHOR = (0.50, 0.73)
    DEFAULT_X_SCALE = 1.0
    DEFAULT_BOX_SCALE = 1.0
    DEFAULT_START_SCALE = 1.0

    def __init__(self, mgr: SceneManager):
        super().__init__(mgr)

        # Load Excel (ID -> Name)
        self.id_map: Dict[str, str] = {}
        self.excel_error: Optional[str] = None
        self._load_excel()

        # Load layout
        sc2 = "scene2"
        self.x_anchor = tuple(self.mgr.layout.get_anchor(sc2, "x_anchor", self.DEFAULT_X_ANCHOR))
        self.box_anchor = tuple(self.mgr.layout.get_anchor(sc2, "box_anchor", self.DEFAULT_BOX_ANCHOR))
        self.start_anchor = tuple(self.mgr.layout.get_anchor(sc2, "start_anchor", self.DEFAULT_START_ANCHOR))
        self.x_scale_mult = self.mgr.layout.get_float(sc2, "x_scale_mult", self.DEFAULT_X_SCALE)
        self.box_scale_mult = self.mgr.layout.get_float(sc2, "box_scale_mult", self.DEFAULT_BOX_SCALE)
        self.start_scale_mult = self.mgr.layout.get_float(sc2, "start_scale_mult", self.DEFAULT_START_SCALE)

        # Assets
        self.missing_assets: List[str] = []
        for p in (SC2_BG_PATH, SC2_X_PATH, SC2_START_PATH, SC2_INPUTBOX_PATH):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))

        self.bg_raw = None
        self.bg = None
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_pos = (0, 0)
        self.bg_scale = 1.0

        self.btn_x: Optional[ImageButton] = None
        self.btn_start: Optional[ImageButton] = None
        self.input_box_img: Optional[pygame.Surface] = None
        self.input_box_rect = pygame.Rect(0, 0, 0, 0)

        if not self.missing_assets:
            self._load_assets()

        # Input state
        self.input_text = ""
        self.focus_input = True
        self.caret_timer = 0.0
        self.caret_on = True

        # Overlay typewriter
        self.mode = "form"  # "form" | "success" | "error"
        self.full_text = ""
        self.shown_text = ""
        self.type_i = 0
        self.type_acc = 0.0
        self.type_interval = 0.05
        self.overlay_ready = False

    def _load_excel(self):
        try:
            import openpyxl  # type: ignore
        except Exception:
            self.excel_error = "Missing dependency: openpyxl. Run: pip install openpyxl"
            return

        if not file_exists(INDEX_XLSX_PATH):
            self.excel_error = f"Missing file: {os.path.basename(INDEX_XLSX_PATH)}"
            return

        try:
            wb = openpyxl.load_workbook(INDEX_XLSX_PATH)
            ws = wb.active
            rows = list(ws.iter_rows(values_only=True))
            if not rows:
                self.excel_error = "INDEX.xlsx is empty"
                return

            start_i = 0
            first = rows[0]
            if first and any(isinstance(x, str) and "id" in x.lower() for x in first if x):
                start_i = 1

            m: Dict[str, str] = {}
            for r in rows[start_i:]:
                if not r:
                    continue
                raw_id = r[0] if len(r) > 0 else None
                raw_name = r[1] if len(r) > 1 else None
                if raw_id is None or raw_name is None:
                    continue
                sid = str(raw_id).strip()
                name = str(raw_name).strip()
                if sid:
                    m[sid] = name

            self.id_map = m
            self.excel_error = None
        except Exception as e:
            self.excel_error = f"Excel read error: {e}"

    def _load_assets(self):
        self.bg_raw = load_bg(SC2_BG_PATH)
        self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
        self.bg_pos = self.bg_rect.topleft

        x_raw = load_button(SC2_X_PATH, colorkey=(0, 0, 0))
        start_raw = load_button(SC2_START_PATH, colorkey=(0, 0, 0))
        box_raw = load_button(SC2_INPUTBOX_PATH, colorkey=(0, 0, 0))

        self.btn_x = ImageButton(x_raw, anchor=self.x_anchor, scale_mult=self.x_scale_mult, use_mask=False, smooth=False)
        self.btn_start = ImageButton(start_raw, anchor=self.start_anchor, scale_mult=self.start_scale_mult, use_mask=False, smooth=False)

        self.btn_x.rebuild(self.bg_rect, self.bg_scale)
        self.btn_start.rebuild(self.bg_rect, self.bg_scale)

        # input box (không phải button => không click sfx)
        s = self.bg_scale * self.box_scale_mult
        bw = max(1, int(box_raw.get_width() * s))
        bh = max(1, int(box_raw.get_height() * s))
        self.input_box_img = pygame.transform.scale(box_raw, (bw, bh))
        self.input_box_rect = self.input_box_img.get_rect(center=anchor_to_point(self.bg_rect, self.box_anchor))

    def _start_overlay(self, mode: str, text: str):
        self.mode = mode  # "success" | "error"
        self.full_text = text
        self.shown_text = ""
        self.type_i = 0
        self.type_acc = 0.0
        self.overlay_ready = False

    def _submit(self):
        sid = self.input_text.strip()
        if sid in self.id_map:
            name = self.id_map[sid]

            # lưu cho scene sau dùng
            self.mgr.player_id = sid
            self.mgr.player_name = name

            self._start_overlay("success", f"Hello {name}")
        else:
            self._start_overlay("error", "Sorry, maybe you are not DA0001's member, please try it again")

    def _back_to_form(self):
        self.mode = "form"
        self.input_text = ""
        self.focus_input = True
        self.overlay_ready = False

    def _go_next_scene(self):
        self.mgr.go_to(Scene3(self.mgr))

    def handle_event(self, event: pygame.event.Event):
        if self.missing_assets:
            return

        # overlay mode
        if self.mode in ("success", "error"):
            if event.type == pygame.KEYDOWN and self.overlay_ready and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                if self.mode == "error":
                    self._back_to_form()
                else:
                    self._go_next_scene()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.overlay_ready:
                if self.mode == "error":
                    self._back_to_form()
                else:
                    self._go_next_scene()
            return

        # form mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self._submit()
                return

            if not self.focus_input:
                return

            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
                return

            ch = event.unicode
            if ch:
                if ch.isalnum() or ch in "_-":
                    if len(self.input_text) < 20:
                        self.input_text += ch

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # click buttons
            if self.btn_x and self.btn_x.handle_event(event):
                pass  # click is only confirmed on MOUSEBUTTONUP
            if self.btn_start and self.btn_start.handle_event(event):
                pass

            # focus input box
            if self.input_box_rect.collidepoint(event.pos):
                self.focus_input = True
            else:
                self.focus_input = False

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.btn_x and self.btn_x.handle_event(event):
                self.mgr.audio.sfx("click")
                self.mgr.go_to(TitleScene(self.mgr))
                return
            if self.btn_start and self.btn_start.handle_event(event):
                self.mgr.audio.sfx("click")
                self._submit()
                return

    def update(self, dt: float):
        self.caret_timer += dt
        if self.caret_timer >= 0.45:
            self.caret_timer = 0.0
            self.caret_on = not self.caret_on

        mp = pygame.mouse.get_pos()

        if self.mode in ("success", "error"):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            if not self.overlay_ready:
                self.type_acc += dt
                while self.type_acc >= self.type_interval and self.type_i < len(self.full_text):
                    self.type_acc -= self.type_interval
                    self.type_i += 1
                    self.shown_text = self.full_text[:self.type_i]
                if self.type_i >= len(self.full_text):
                    self.overlay_ready = True
            return

        # hover cursor
        hover_hand = False
        if self.btn_x:
            self.btn_x.update_hover(mp)
            hover_hand |= self.btn_x.hovered
        if self.btn_start:
            self.btn_start.update_hover(mp)
            hover_hand |= self.btn_start.hovered

        if hover_hand:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        elif self.input_box_rect.collidepoint(mp):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))

        if self.missing_assets or self.bg is None:
            t = self.mgr.fonts.fallback(22).render("Scene 2 assets missing:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return

        screen.blit(self.bg, self.bg_pos)

        # UI
        if self.input_box_img:
            screen.blit(self.input_box_img, self.input_box_rect.topleft)
        if self.btn_start:
            self.btn_start.draw(screen)
        if self.btn_x:
            self.btn_x.draw(screen)

        f_main = self.mgr.fonts.pressstart(18)
        f_small = self.mgr.fonts.pressstart(14)

        # input text in box
        if self.mode == "form":
            inner = self.input_box_rect.inflate(-40, -30)
            txt_show = self.input_text + ("|" if (self.focus_input and self.caret_on) else "")
            surf = f_main.render(txt_show, True, (20, 20, 20))
            if surf.get_width() > inner.w:
                surf = f_main.render(txt_show[-12:], True, (20, 20, 20))
            screen.blit(surf, (inner.x + 10, inner.y + inner.h // 2 - surf.get_height() // 2))

        # excel warning
        if self.excel_error and self.mode == "form":
            warn = f_small.render(self.excel_error, True, (255, 255, 255))
            screen.blit(warn, (self.bg_rect.x + 20, self.bg_rect.bottom - 40))

        # overlay
        if self.mode in ("success", "error"):
            overlay = pygame.Surface((WINDOW_W, WINDOW_H))
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            msg = f_main.render(self.shown_text, True, (255, 255, 255))
            screen.blit(msg, (WINDOW_W // 2 - msg.get_width() // 2, WINDOW_H // 2 - msg.get_height() // 2))

            if self.overlay_ready:
                hint = f_small.render("Click / Enter / Space to continue", True, (255, 255, 255))
                screen.blit(hint, (WINDOW_W // 2 - hint.get_width() // 2, WINDOW_H // 2 + 60))


# ---------- Video scenes (3/4/7/11/16/20/22/24/26/28) ----------

class Scene3(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC3_VIDEO_PATH, next_scene_factory=lambda m: Scene4(m), loop=False)

class Scene4(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        # Scene4: loop video (context2.mp4), vẫn cho skip để qua Scene5
        super().__init__(mgr, SC4_VIDEO_PATH, next_scene_factory=lambda m: Scene5(m), loop=True)

class Scene7(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC7_VIDEO_PATH, next_scene_factory=lambda m: Scene8(m), loop=False)

class Scene11(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC11_VIDEO_PATH, next_scene_factory=lambda m: Scene12(m), loop=False)

class Scene16(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC16_VIDEO_PATH, next_scene_factory=lambda m: Scene17(m), loop=False)

class Scene20(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC20_VIDEO_PATH, next_scene_factory=lambda m: Scene21(m), loop=False)

class Scene22(VideoCutsceneNoBgm): 
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC22_VIDEO_PATH, next_scene_factory=lambda m: Scene23(m), loop=False)

class Scene24(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC24_VIDEO_PATH, next_scene_factory=lambda m: Scene25(m), loop=False)

class Scene26(VideoCutsceneNoBgm): 
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC26_VIDEO_PATH, next_scene_factory=lambda m: Scene27(m), loop=False)

class Scene28(VideoCutscene):
    def __init__(self, mgr: SceneManager):
        super().__init__(mgr, SC28_VIDEO_PATH, next_scene_factory=lambda m: Scene29(m), loop=False)


# ---------- Input scenes (5/14/18/21/25) + Scene9 special ----------

class Scene5(TextAnswerScene):
    ANSWER = "EARTH_GRAVITY_CONSTANT=9.8"

    def __init__(self, mgr: SceneManager):
        def check(ans: str) -> bool:
            return ans == Scene5.ANSWER

        def char_ok(ch: str) -> bool:
            return ch.isalnum() or ch in "_=."

        super().__init__(
            mgr,
            bg_path=SC5_BG_PATH,
            input_path=SC5_INPUT_PATH,
            layout_key="scene5",
            answer_check=check,
            next_scene_factory=lambda m: Scene6(m),
            wrong_text="You can try again, fighting!!!",
            max_len=40,
            char_filter=char_ok,
        )

class Scene6(DonePopupScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC6_BG_PATH,
            layout_key="scene6",
            next_scene_factory=lambda m: BlackTextTransitionScene(
                m,
                text="floor 5...",
                next_scene_factory=lambda mm: Scene7(mm),
                min_lock=0.5
            )
        )

class Scene8(Scene):
    """
    Scene 8: Password / Forgot
    - Click PASSWORD: hiện overlay "Oops..."
    - Click FORGOT  : fade out -> Scene9
    """
    BGM_KEY = "input"

    DEFAULT_PASSWORD_ANCHOR = (0.50, 0.54)
    DEFAULT_FORGOT_ANCHOR = (0.50, 0.70)
    DEFAULT_PASSWORD_SCALE = 1.0
    DEFAULT_FORGOT_SCALE = 1.0

    def __init__(self, mgr: SceneManager):
        super().__init__(mgr)

        self.mode = "normal"  # "normal" | "overlay"
        self.fade = False
        self.fade_t = 0.0
        self.fade_duration = 0.8

        self.missing_assets: List[str] = []
        for p in (SC8_BG_PATH, SC8_PASSWORD_PATH, SC8_FORGOT_PATH):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))

        self.bg_raw = None
        self.bg = None
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_pos = (0, 0)
        self.bg_scale = 1.0

        self.btn_password: Optional[ImageButton] = None
        self.btn_forgot: Optional[ImageButton] = None

        # layout
        a_pw = tuple(self.mgr.layout.get_anchor("scene8", "password_anchor", self.DEFAULT_PASSWORD_ANCHOR))
        a_fg = tuple(self.mgr.layout.get_anchor("scene8", "forgot_anchor", self.DEFAULT_FORGOT_ANCHOR))
        s_pw = self.mgr.layout.get_float("scene8", "password_scale_mult", self.DEFAULT_PASSWORD_SCALE)
        s_fg = self.mgr.layout.get_float("scene8", "forgot_scale_mult", self.DEFAULT_FORGOT_SCALE)

        if not self.missing_assets:
            self.bg_raw = load_bg(SC8_BG_PATH)
            self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
            self.bg_pos = self.bg_rect.topleft

            pw_raw = load_button(SC8_PASSWORD_PATH, colorkey=(0, 0, 0))
            fg_raw = load_button(SC8_FORGOT_PATH, colorkey=(0, 0, 0))

            self.btn_password = ImageButton(pw_raw, anchor=a_pw, scale_mult=s_pw, use_mask=True, smooth=False)
            self.btn_forgot = ImageButton(fg_raw, anchor=a_fg, scale_mult=s_fg, use_mask=True, smooth=False)

            self.btn_password.rebuild(self.bg_rect, self.bg_scale)
            self.btn_forgot.rebuild(self.bg_rect, self.bg_scale)

    def handle_event(self, event: pygame.event.Event):
        if self.missing_assets:
            return

        if self.fade:
            return

        # overlay: any click/enter/space to close overlay
        if self.mode == "overlay":
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                self.mode = "normal"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mode = "normal"
            return

        # normal mode: handle buttons
        if self.btn_password and self.btn_password.handle_event(event):
            # click sound only on object
            self.mgr.audio.sfx("click")
            self.mode = "overlay"
            return

        if self.btn_forgot and self.btn_forgot.handle_event(event):
            self.mgr.audio.sfx("click")
            self.fade = True
            self.fade_t = 0.0
            return

    def update(self, dt: float):
        if self.missing_assets:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        if self.fade:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            self.fade_t += dt
            if self.fade_t >= self.fade_duration:
                self.mgr.go_to(Scene9(self.mgr))
            return

        if self.mode == "overlay":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        mp = pygame.mouse.get_pos()
        hover_hand = False
        if self.btn_password:
            self.btn_password.update_hover(mp)
            hover_hand |= self.btn_password.hovered
        if self.btn_forgot:
            self.btn_forgot.update_hover(mp)
            hover_hand |= self.btn_forgot.hovered
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if hover_hand else pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))

        if self.missing_assets or self.bg is None:
            t = self.mgr.fonts.fallback(22).render("Scene 8 assets missing:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return

        screen.blit(self.bg, self.bg_pos)
        if self.btn_password:
            self.btn_password.draw(screen)
        if self.btn_forgot:
            self.btn_forgot.draw(screen)

        # overlay message
        if self.mode == "overlay":
            overlay = pygame.Surface((WINDOW_W, WINDOW_H))
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))
            f = self.mgr.fonts.pressstart(18)
            msg = f.render("Oops... you forgot your password!", True, (255, 255, 255))
            screen.blit(msg, (WINDOW_W // 2 - msg.get_width() // 2, WINDOW_H // 2 - msg.get_height() // 2))
            hint = self.mgr.fonts.pressstart(14).render("Click/ Enter/ Space to continue", True, (255, 255, 255))
            screen.blit(hint, (WINDOW_W // 2 - hint.get_width() // 2, WINDOW_H // 2 + 60))

        # fade out
        if self.fade:
            a = int(255 * min(1.0, self.fade_t / self.fade_duration))
            fade_surf = pygame.Surface((WINDOW_W, WINDOW_H))
            fade_surf.set_alpha(a)
            fade_surf.fill((0, 0, 0))
            screen.blit(fade_surf, (0, 0))


class Scene9(Scene):
    """
    Scene 9: Input password dạng dictionary access:
      MY_PASSWORD['<ID>'] hoặc MY_PASSWORD["<ID>"]
    - <ID> lấy từ Scene2 (mgr.player_id)
    """
    BGM_KEY = "input"

    DEFAULT_INPUT_ANCHOR = (0.50, 0.58)
    DEFAULT_INPUT_SCALE = 1.0

    def __init__(self, mgr: SceneManager):
        super().__init__(mgr)

        self.player_id = self.mgr.player_id

        self.mode = "form"  # "form" | "error" | "missing_id"
        self.input_text = ""
        self.focus_input = True
        self.caret_timer = 0.0
        self.caret_on = True

        self.error_text = "Sorry, your password is incorrect. Come on, try again!"
        self.missing_id_text = "Missing player ID. Please start from Scene 2."

        # layout
        self.input_anchor = tuple(self.mgr.layout.get_anchor("scene9", "input_anchor", self.DEFAULT_INPUT_ANCHOR))
        self.input_scale_mult = self.mgr.layout.get_float("scene9", "input_scale_mult", self.DEFAULT_INPUT_SCALE)

        self.missing_assets: List[str] = []
        for p in (SC9_BG_PATH, SC9_INPUT_PATH):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))

        self.bg_raw = None
        self.bg = None
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_pos = (0, 0)
        self.bg_scale = 1.0

        self.input_raw = None
        self.input_img = None
        self.input_rect = pygame.Rect(0, 0, 0, 0)

        if not self.missing_assets:
            self.bg_raw = load_bg(SC9_BG_PATH)
            self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
            self.bg_pos = self.bg_rect.topleft

            self.input_raw = load_button(SC9_INPUT_PATH, colorkey=(0, 0, 0))
            self._rebuild()

        if not self.player_id:
            self.mode = "missing_id"
            self.focus_input = False

    def _rebuild(self):
        if self.input_raw is None:
            return
        s = self.bg_scale * self.input_scale_mult
        w = max(1, int(self.input_raw.get_width() * s))
        h = max(1, int(self.input_raw.get_height() * s))
        self.input_img = pygame.transform.scale(self.input_raw, (w, h))
        self.input_rect = self.input_img.get_rect(center=anchor_to_point(self.bg_rect, self.input_anchor))

    def _expected_answers(self):
        pid = str(self.player_id)
        return (f"MY_PASSWORD['{pid}']", f'MY_PASSWORD["{pid}"]')

    def _submit(self):
        ans = self.input_text.strip()

        # reject spaces anywhere
        if " " in ans:
            self.mode = "error"
            self.focus_input = False
            return

        exp1, exp2 = self._expected_answers()
        if ans == exp1 or ans == exp2:
            self.mgr.audio.sfx("correct")
            self.mgr.go_to(Scene10(self.mgr))
        else:
            self.mgr.audio.sfx("wrong")
            self.mode = "error"
            self.focus_input = False

    def _back_to_form(self):
        self.mode = "form"
        self.input_text = ""
        self.focus_input = True

    def handle_event(self, event: pygame.event.Event):
        if self.missing_assets:
            return

        # missing id overlay -> go back scene2
        if self.mode == "missing_id":
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                self.mgr.go_to(Scene2(self.mgr))
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.mgr.go_to(Scene2(self.mgr))
            return

        # error overlay
        if self.mode == "error":
            if event.type == pygame.KEYDOWN and event.key in (pygame.K_SPACE, pygame.K_RETURN):
                self._back_to_form()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self._back_to_form()
            return

        # form
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self._submit()
                return

            if not self.focus_input:
                return

            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
                return

            ch = event.unicode
            if ch:
                if ch == " ":
                    return
                allowed = "[]_\"'().,-"
                if ch.isalnum() or ch in allowed:
                    if len(self.input_text) < 60:
                        self.input_text += ch

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.input_rect.collidepoint(event.pos):
                self.focus_input = True
            else:
                self.focus_input = False

    def update(self, dt: float):
        self.caret_timer += dt
        if self.caret_timer >= 0.45:
            self.caret_timer = 0.0
            self.caret_on = not self.caret_on

        if self.missing_assets:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        if self.mode != "form":
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        mp = pygame.mouse.get_pos()
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM if self.input_rect.collidepoint(mp) else pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen: pygame.Surface):
        if self.missing_assets:
            screen.fill((10, 10, 10))
            t = self.mgr.fonts.fallback(22).render("Scene 9 assets missing:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return

        screen.fill((0, 0, 0))
        screen.blit(self.bg, self.bg_pos)

        if self.input_img:
            screen.blit(self.input_img, self.input_rect.topleft)

        f_main = self.mgr.fonts.pressstart(18)
        f_small = self.mgr.fonts.pressstart(14)

        if self.mode == "form":
            inner = self.input_rect.inflate(-40, -30)
            txt_show = self.input_text + ("|" if (self.focus_input and self.caret_on) else "")
            surf = f_main.render(txt_show, True, (20, 20, 20))
            if surf.get_width() > inner.w:
                surf = f_main.render(txt_show[-30:], True, (20, 20, 20))
            screen.blit(surf, (inner.x + 10, inner.y + inner.h // 2 - surf.get_height() // 2))

        if self.mode in ("error", "missing_id"):
            overlay = pygame.Surface((WINDOW_W, WINDOW_H))
            overlay.fill((0, 0, 0))
            screen.blit(overlay, (0, 0))

            msg_text = self.error_text if self.mode == "error" else self.missing_id_text
            msg = f_main.render(msg_text, True, (255, 255, 255))
            screen.blit(msg, (WINDOW_W // 2 - msg.get_width() // 2, WINDOW_H // 2 - msg.get_height() // 2))

            hint = f_small.render("Click / Enter/ Space to continue", True, (255, 255, 255))
            screen.blit(hint, (WINDOW_W // 2 - hint.get_width() // 2, WINDOW_H // 2 + 60))


class Scene10(DonePopupScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC10_BG_PATH,
            layout_key="scene10",
            next_scene_factory=lambda m: BlackTextTransitionScene(
                m,
                text="floor 4...",
                next_scene_factory=lambda mm: Scene11(mm),
                min_lock=0.5
            )
        )


class Scene12(ClickObjectScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC12_BG_PATH,
            obj_path=SC12_LAPTOP_PATH,
            layout_key="scene12",
            anchor_field="laptop_anchor",
            scale_field="laptop_scale_mult",
            default_anchor=(0.52, 0.54),
            default_scale=1.0,
            next_scene_factory=lambda m: Scene13(m),
            use_mask=True,
            allow_keys=False,
            obj_colorkey=None,
        )


# ---------- Scene 13 (Dataset) - custom (scroll + highlight) ----------

class Scene13(Scene):
    """
    Scene 13: Hiển thị Dataset (đọc từ Dataset.xlsx) trong "màn hình data".
    - Scroll bằng wheel, và click arrow để scroll nhanh
    - Click NEXT để sang Scene14
    - Highlight ô header "ecneicS retupmoC" (đã đảo chữ)
    """
    BGM_KEY = "input"

    # Defaults (giữ đúng key layout cũ)
    D_SCREEN_ANCHOR = (0.52, 0.42)
    D_ARROW_ANCHOR  = (0.70, 0.44)
    D_NEXT_ANCHOR   = (0.80, 0.78)

    D_SCREEN_SCALE = 1.00
    D_ARROW_SCALE  = 1.00
    D_NEXT_SCALE   = 1.00

    # Viewport inset inside screen image (L,T,R,B) in screen-image pixels (pre-scale)
    D_SCREEN_INSET = [32, 26, 32, 52]

    MAX_ROWS = 250
    MAX_COLS = 10

    WHEEL_STEP = 70
    ARROW_STEP = 140

    TARGET_HEADER = "ecneicS retupmoC"
    PULSE_PERIOD = 1.0

    def __init__(self, mgr: SceneManager):
        super().__init__(mgr)

        self.missing_assets: List[str] = []
        for p in (SC13_BG_PATH, SC13_SCREEN_PATH, SC13_ARROW_PATH, SC13_NEXT_PATH, DATASET_XLSX_PATH):
            if not file_exists(p):
                self.missing_assets.append(os.path.basename(p))

        self.font = self.mgr.fonts.pressstart(16)

        # bg letterbox
        self.bg_raw = None
        self.bg = None
        self.bg_rect = pygame.Rect(0, 0, 0, 0)
        self.bg_pos = (0, 0)
        self.bg_scale = 1.0

        # objects
        self.screen_raw = None
        self.arrow_raw = None
        self.next_raw = None

        self.screen_img = None
        self.screen_rect = pygame.Rect(0, 0, 0, 0)

        self.arrow_btn: Optional[ImageButton] = None
        self.next_btn: Optional[ImageButton] = None

        self.viewport_rect = pygame.Rect(0, 0, 0, 0)

        # dataset surfaces
        self.scroll_y = 0
        self.data_content: Optional[pygame.Surface] = None
        self.data_scaled: Optional[pygame.Surface] = None
        self.data_scale = 1.0
        self.data_w = 0
        self.data_h = 0
        self.hcell_rect: Optional[pygame.Rect] = None

        # animation
        self.t = 0.0
        self.glitch_timer = 0.0
        self.glitch_on = False

        if not self.missing_assets:
            self._load_assets()
            self._load_layout()
            self._rebuild_objects()
            self._build_dataset_surface()
            self._rebuild_scaled_dataset()

    def _load_assets(self):
        self.bg_raw = load_bg(SC13_BG_PATH)
        self.bg, self.bg_rect, self.bg_scale = fit_letterbox(self.bg_raw, WINDOW_W, WINDOW_H)
        self.bg_pos = self.bg_rect.topleft

        self.screen_raw = load_img_alpha(SC13_SCREEN_PATH)
        self.arrow_raw = load_button(SC13_ARROW_PATH, colorkey=(0, 0, 0))
        self.next_raw = load_button(SC13_NEXT_PATH, colorkey=(0, 0, 0))

    def _load_layout(self):
        key = "scene13"
        self.screen_anchor = tuple(self.mgr.layout.get_anchor(key, "screen_anchor", self.D_SCREEN_ANCHOR))
        self.arrow_anchor = tuple(self.mgr.layout.get_anchor(key, "arrow_anchor", self.D_ARROW_ANCHOR))
        self.next_anchor = tuple(self.mgr.layout.get_anchor(key, "next_anchor", self.D_NEXT_ANCHOR))

        self.screen_scale_mult = self.mgr.layout.get_float(key, "screen_scale_mult", self.D_SCREEN_SCALE)
        self.arrow_scale_mult = self.mgr.layout.get_float(key, "arrow_scale_mult", self.D_ARROW_SCALE)
        self.next_scale_mult = self.mgr.layout.get_float(key, "next_scale_mult", self.D_NEXT_SCALE)

        self.screen_inset = self.mgr.layout.get_inset4(key, "screen_inset", self.D_SCREEN_INSET)

    def _scale_obj(self, raw: pygame.Surface, mult: float, smooth: bool = False) -> pygame.Surface:
        s = self.bg_scale * mult
        w = max(1, int(raw.get_width() * s))
        h = max(1, int(raw.get_height() * s))
        return pygame.transform.smoothscale(raw, (w, h)) if smooth else pygame.transform.scale(raw, (w, h))

    def _rebuild_objects(self):
        self.screen_img = self._scale_obj(self.screen_raw, self.screen_scale_mult, smooth=False)
        self.screen_rect = self.screen_img.get_rect(center=anchor_to_point(self.bg_rect, self.screen_anchor))
        # Arrow / Next: KHÔNG scale trước rồi hack nữa.
        # Làm đúng như main.py: dùng raw + scale_mult, rồi rebuild theo bg_rect/bg_scale.
        self.arrow_btn = ImageButton(self.arrow_raw, anchor=self.arrow_anchor, scale_mult=self.arrow_scale_mult, use_mask=True, smooth=False)
        self.next_btn  = ImageButton(self.next_raw,  anchor=self.next_anchor,  scale_mult=self.next_scale_mult,  use_mask=True, smooth=False)

        self.arrow_btn.rebuild(self.bg_rect, self.bg_scale)
        self.next_btn.rebuild(self.bg_rect, self.bg_scale)

        # viewport inside screen
        L, T, R, B = self.screen_inset
        k = self.bg_scale * self.screen_scale_mult
        l, t, r, b = int(L * k), int(T * k), int(R * k), int(B * k)
        self.viewport_rect = pygame.Rect(
            self.screen_rect.x + l,
            self.screen_rect.y + t,
            max(1, self.screen_rect.w - l - r),
            max(1, self.screen_rect.h - t - b),
        )
        self._clamp_scroll()

    # -------- Dataset render (Excel -> Surface) --------
    def _build_dataset_surface(self):
        try:
            import openpyxl  # type: ignore
        except Exception:
            self.data_content = None
            return

        wb = openpyxl.load_workbook(DATASET_XLSX_PATH, data_only=True)
        ws = wb.active

        rows: List[List[str]] = []
        for i, r in enumerate(ws.iter_rows(values_only=True)):
            rows.append([("" if v is None else str(v)) for v in r])
            if i >= self.MAX_ROWS:
                break
        if not rows:
            self.data_content = None
            return

        header = rows[0][: self.MAX_COLS]
        body = [rr[: self.MAX_COLS] for rr in rows[1:]]

        # ----- WHITE THEME (nền trắng, chữ đen) -----
        pad = 12
        min_w, max_w = 90, 280
        col_w = []
        for c in range(len(header)):
            sample = [header[c]] + [body[i][c] for i in range(min(len(body), 18))]
            w = max(self.font.size(s)[0] for s in sample) + pad * 2
            col_w.append(max(min_w, min(max_w, w)))

        header_h = 42
        row_h = 34
        W = sum(col_w) + 2
        H = header_h + len(body) * row_h + 2

        surf = pygame.Surface((W, H), pygame.SRCALPHA)
        surf.fill((255, 255, 255, 255))  # nền trắng

        # header background hơi xám để phân biệt
        pygame.draw.rect(surf, (235, 235, 235, 255), (0, 0, W, header_h))

        grid = (170, 170, 170, 255)
        text_col = (15, 15, 15)

        x = 0
        self.hcell_rect = None
        for c, name in enumerate(header):
            pygame.draw.line(surf, grid, (x, 0), (x, H), 1)
            txt = self.font.render(name, True, text_col)
            surf.blit(txt, (x + pad, header_h // 2 - txt.get_height() // 2))
            if name.strip() == self.TARGET_HEADER:
                self.hcell_rect = pygame.Rect(x, 0, col_w[c], header_h)
            x += col_w[c]
        pygame.draw.line(surf, grid, (W - 1, 0), (W - 1, H), 1)
        pygame.draw.line(surf, grid, (0, header_h), (W, header_h), 1)

        y = header_h
        for r_i, rr in enumerate(body):
            if r_i % 2 == 0:
                pygame.draw.rect(surf, (248, 248, 248, 255), (0, y, W, row_h))
            x = 0
            for c, cell in enumerate(rr):
                s = cell
                if self.font.size(s)[0] > col_w[c] - pad * 2:
                    s = s[:18] + "..."
                txt = self.font.render(s, True, text_col)
                surf.blit(txt, (x + pad, y + row_h // 2 - txt.get_height() // 2))
                x += col_w[c]
            pygame.draw.line(surf, grid, (0, y + row_h), (W, y + row_h), 1)
            y += row_h

        self.data_content = surf
        self.data_w, self.data_h = W, H
        self.scroll_y = 0

    def _rebuild_scaled_dataset(self):
        if self.data_content is None:
            self.data_scaled = None
            return
        vw = max(1, self.viewport_rect.w)
        self.data_scale = min(1.0, vw / max(1, self.data_w))
        sw = max(1, int(self.data_w * self.data_scale))
        sh = max(1, int(self.data_h * self.data_scale))
        self.data_scaled = pygame.transform.smoothscale(self.data_content, (sw, sh))
        self._clamp_scroll()

    def _clamp_scroll(self):
        if self.data_scaled is None:
            self.scroll_y = 0
            return
        vh = self.viewport_rect.h
        ch = self.data_scaled.get_height()
        if ch <= vh:
            self.scroll_y = 0
            return
        max_down = ch - vh
        if self.scroll_y > 0:
            self.scroll_y = 0
        if self.scroll_y < -max_down:
            self.scroll_y = -max_down

    def handle_event(self, event: pygame.event.Event):
        if self.missing_assets:
            return

        # scroll
        if event.type == pygame.MOUSEWHEEL:
            if self.viewport_rect.collidepoint(pygame.mouse.get_pos()):
                self.scroll_y += (self.WHEEL_STEP * event.y)
                self._clamp_scroll()

        # click arrow/next
        if self.arrow_btn and self.arrow_btn.handle_event(event):
            self.mgr.audio.sfx("click")
            self.scroll_y -= self.ARROW_STEP
            self._clamp_scroll()

        if self.next_btn and self.next_btn.handle_event(event):
            self.mgr.audio.sfx("click")
            self.mgr.go_to(Scene14(self.mgr))

    def update(self, dt: float):
        self.t += dt
        mp = pygame.mouse.get_pos()

        if self.missing_assets:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            return

        hover_any = False
        if self.next_btn:
            self.next_btn.update_hover(mp)
            hover_any |= self.next_btn.hovered
        if self.arrow_btn:
            self.arrow_btn.update_hover(mp)
            hover_any |= self.arrow_btn.hovered
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND if hover_any else pygame.SYSTEM_CURSOR_ARROW)

        # glitch pulse
        self.glitch_timer -= dt
        if self.glitch_timer <= 0:
            if random.random() < 0.08:
                self.glitch_on = True
                self.glitch_timer = 0.04
            else:
                self.glitch_on = False
                self.glitch_timer = random.uniform(0.10, 0.25)

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))
        if self.missing_assets or self.bg is None:
            t = self.mgr.fonts.fallback(22).render("Scene 13 missing assets:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return

        screen.blit(self.bg, self.bg_pos)

        # layer 1: screen frame
        screen.blit(self.screen_img, self.screen_rect.topleft)

        # layer 2: dataset clipped
        if self.data_scaled is not None:
            old_clip = screen.get_clip()
            screen.set_clip(self.viewport_rect)

            dx = self.viewport_rect.x
            dy = self.viewport_rect.y + int(self.scroll_y)
            screen.blit(self.data_scaled, (dx, dy))

            # highlight target header cell
            if self.hcell_rect is not None:
                k = 0.5 + 0.5 * math.sin((self.t / self.PULSE_PERIOD) * 2.0 * math.pi)
                alpha = int(80 + 120 * k)

                r = pygame.Rect(
                    dx + int(self.hcell_rect.x * self.data_scale),
                    dy + int(self.hcell_rect.y * self.data_scale),
                    int(self.hcell_rect.w * self.data_scale),
                    int(self.hcell_rect.h * self.data_scale),
                )

                if r.colliderect(self.viewport_rect):
                    if self.glitch_on:
                        r.x += random.randint(-2, 2)
                        r.y += random.randint(-1, 1)
                        alpha = min(220, alpha + 40)

                    # semi transparent yellow fill (hợp nền trắng)
                    fill = pygame.Surface((r.w, r.h), pygame.SRCALPHA)
                    fill.fill((255, 255, 0, int(alpha * 0.25)))
                    screen.blit(fill, r.topleft)

                    # blue border
                    border = pygame.Surface((r.w + 8, r.h + 8), pygame.SRCALPHA)
                    pygame.draw.rect(border, (0, 120, 255, alpha), border.get_rect(), 3, border_radius=8)
                    screen.blit(border, (r.x - 4, r.y - 4))

            screen.set_clip(old_clip)

        # layer 3: arrow + next
        if self.arrow_btn:
            self.arrow_btn.draw(screen)
        if self.next_btn:
            self.next_btn.draw(screen)


class Scene14(TextAnswerScene):
    ANSWER = "HEADER[::-1]"
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC14_BG_PATH,
            input_path=SC14_INPUT_PATH,
            layout_key="scene14",
            answer_check=lambda ans: ans.strip() == Scene14.ANSWER,
            next_scene_factory=lambda m: Scene15(m),
            wrong_text="Try again, you almost got it!",
            max_len=120,
            char_filter=lambda ch: ch.isprintable() and ch not in "\t\r\n",
        )


class Scene15(DonePopupScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC15_BG_PATH,
            layout_key="scene15",
            next_scene_factory=lambda m: BlackTextTransitionScene(
                m,
                text="floor 3...",
                next_scene_factory=lambda mm: Scene16(mm),
                min_lock=0.5
            )
        )



class Scene17(ClickObjectScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC17_BG_PATH,
            obj_path=SC17_NEXT_PATH,
            layout_key="scene17",
            anchor_field="next_anchor",
            scale_field="next_scale_mult",
            default_anchor=(0.88, 0.86),
            default_scale=1.0,
            next_scene_factory=lambda m: Scene18(m),
            use_mask=True,
            allow_keys=True,  # Enter/Space cũng được qua màn (không click sfx)
        )


class Scene18(TextAnswerScene):
    ANSWER = "np.array([[1,0,1],[1,1,0],[0,1,-2]])"
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC18_BG_PATH,
            input_path=SC18_INPUT_PATH,
            layout_key="scene18",
            answer_check=lambda ans: ans.strip() == Scene18.ANSWER,
            next_scene_factory=lambda m: Scene19(m),
            wrong_text="Wrong answer. Try again!",
            max_len=140,
            char_filter=lambda ch: ch.isprintable() and ch not in "\t\r\n",
            back_button=(SC18_BACK_PATH, "back", (0.12, 0.18), 1.0, lambda m: Scene17(m)),
        )


class Scene19(DonePopupScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC19_BG_PATH,
            layout_key="scene19",
            next_scene_factory=lambda m: BlackTextTransitionScene(
                m,
                text="floor 2...",
                next_scene_factory=lambda mm: Scene20(mm),
                min_lock=0.5
            )
        )

class Scene21(TextAnswerScene):
    ANSWER = "Math[Math<5]+=1"
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC21_BG_PATH,
            input_path=SC21_INPUT_PATH,
            layout_key="scene21",
            answer_check=lambda ans: ans.strip() == Scene21.ANSWER,
            next_scene_factory=lambda m: Scene22(m),
            wrong_text="Wrong answer. Try again!",
            max_len=120,
        )

class Scene23(DonePopupScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC23_BG_PATH,
            layout_key="scene23",
            next_scene_factory=lambda m: BlackTextTransitionScene(
                m,
                text="floor 1...",
                next_scene_factory=lambda mm: Scene24(mm),
                min_lock=0.5
            )
        )



class Scene25(TextAnswerScene):
    ANSWER = "student.mean()"
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC25_BG_PATH,
            input_path=SC25_INPUT_PATH,
            layout_key="scene25",
            answer_check=lambda ans: ans.strip() == Scene25.ANSWER,
            next_scene_factory=lambda m: Scene26(m),
            wrong_text="Wrong answer. Try again!",
            max_len=80,
        )


class Scene27(DonePopupScene):
    def __init__(self, mgr: SceneManager):
        super().__init__(
            mgr,
            bg_path=SC27_BG_PATH,
            layout_key="scene27",
            next_scene_factory=lambda m: BlackTextTransitionScene(
                m,
                text="you've met teacher Dung",
                next_scene_factory=lambda mm: Scene28(mm),
                min_lock=0.5
            )
        )


class Scene29(Scene):
    """
    Scene 29 (Final):
    - Chỉ hiển thị màn hình kết thúc.
    - ENTER / SPACE / Left Click -> về TitleScene
      (KHÔNG phát click SFX vì đây không phải click object/button)
    """
    BGM_KEY = "title"

    def __init__(self, mgr: SceneManager):
        super().__init__(mgr)
        self.missing_assets: List[str] = []
        if not file_exists(SC29_BG_PATH):
            self.missing_assets.append(os.path.basename(SC29_BG_PATH))

        self.bg_raw = None
        self.bg = None
        self.bg_pos = (0, 0)

        if not self.missing_assets:
            self.bg_raw = load_bg(SC29_BG_PATH)
            s = min(WINDOW_W / self.bg_raw.get_width(), WINDOW_H / self.bg_raw.get_height())
            w = int(self.bg_raw.get_width() * s)
            h = int(self.bg_raw.get_height() * s)
            self.bg = pygame.transform.smoothscale(self.bg_raw, (w, h))
            self.bg_pos = ((WINDOW_W - w) // 2, (WINDOW_H - h) // 2)

    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN and event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.mgr.go_to(TitleScene(self.mgr))
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.mgr.go_to(TitleScene(self.mgr))

    def update(self, dt: float):
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def draw(self, screen: pygame.Surface):
        screen.fill((0, 0, 0))
        if self.missing_assets or self.bg is None:
            t = self.mgr.fonts.fallback(22).render("Scene 29 missing asset:", True, (240, 240, 240))
            screen.blit(t, (60, 80))
            y = 120
            for f in self.missing_assets:
                line = self.mgr.fonts.fallback(20).render(f"- {f}", True, (240, 240, 240))
                screen.blit(line, (90, y))
                y += 30
            return
        screen.blit(self.bg, self.bg_pos)


# ============================================================
# 11) MAIN LOOP
# ============================================================

def main():
    # --- Pygame init (âm thanh ổn định) ---
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    try:
        pygame.mixer.init()
    except Exception:
        # không có audio device -> game vẫn chạy nhưng không có sound
        pass

    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("UEH Library Escape - CS1 Project")

    clock = pygame.time.Clock()

    # shared systems
    fonts = Fonts()
    layout = LayoutStore(LAYOUT_PATH)
    audio = AudioManager()
    mgr = SceneManager(fonts, layout, audio)

    # start scene
    mgr.go_to(TitleScene(mgr), record_history=False)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

            # -------- GLOBAL CONTROLS (đồng nhất toàn game) --------
            # ESC: về Title (trừ khi đang ở TitleScene -> Title tự xử lý quit confirm)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if not isinstance(mgr.scene, TitleScene):
                    mgr.go_to(TitleScene(mgr))
                    continue

            # ` : quay lại scene trước đó (debug)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKQUOTE:
                mgr.back()
                continue

            # pass event to current scene
            if mgr.scene:
                mgr.scene.handle_event(event)

        if not running:
            break

        if mgr.scene:
            mgr.scene.update(dt)
            mgr.scene.draw(screen)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()