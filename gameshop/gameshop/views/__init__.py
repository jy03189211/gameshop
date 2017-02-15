from .index import IndexView
from .search import SearchView
from .categories import CategoriesView
from .dashboard import DashboardView
from .owned_games import OwnedGamesView
from .orders import OrdersView
from .managed_games import ManagedGamesView
from .sales import SalesView
from .new_game import NewGameView
from .game import GameView
from .game_edit import GameEditView, remove_game_view
from .cart import CartView
from .auth import login_view, register_view
from .payment_callback import (
    payment_success_view, payment_cancel_view, payment_error_view)
from .settings import (
    SettingsView,
    become_developer_view, become_developer_done_view,
    public_name_change_view, public_name_change_done_view,
    update_api_settings_view, update_api_settings_done_view
)