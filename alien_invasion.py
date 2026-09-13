import sys
import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    """Ogólna klasa przeznaczona do zarządzania zasobami i sposobem działania
    gry."""
    def __init__(self):
        """Inicjalizacja gry i utworzenie jej zasobów."""
        pygame.init() 
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Inwazja obcych")
        self.ship = Ship(self)
    def run_game(self):
        """Rozpoczęcie pętli głównej gry."""
        while True: 
        # Oczekiwanie na naciśnięcie klawisza lub przycisku myszy.
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(10)

    def _check_events(self):
         for event in pygame.event.get(): 
                if event.type == pygame.QUIT: 
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type==pygame.KEYUP:
                    self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        if event.key==pygame.K_LEFT:
            self.ship.moving_left=True
        if event.key==pygame.K_UP:
            self.ship.moving_up=True
        if event.key==pygame.K_DOWN:
            self.ship.moving_down=True
        if event.key==pygame.K_q:
            sys.exit()
        
    def _check_keyup_events(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        if event.key==pygame.K_LEFT:
            self.ship.moving_left=False
        if event.key==pygame.K_UP:
            self.ship.moving_up=False
        if event.key==pygame.K_DOWN:
            self.ship.moving_down=False

    def _update_screen(self):
            # Odświeżenie ekranu w trakcie każdej iteracji pętli.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
                    # Wyświetlenie ostatnio zmodyfikowanego ekranu.
            pygame.display.flip()

if __name__ == '__main__':
    # Utworzenie egzemplarza gry i jej uruchomienie.
    ai = AlienInvasion()
    ai.run_game()                                                                      
