" README
" Structure created and maintained by Michael Stolarz (stoladev).
" Far from perfect. Definitely not optimized. Use at your own risk.


" Autocmd Commands
autocmd! BufWritePost sysinit.vim source %
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview
au VimEnter * NERDTree


" Keybinds
nnoremap ; :


" Tab and Indent Settings
set tabstop=4
set softtabstop=4
set shiftwidth=4
set shiftround
set expandtab
set autoindent
set smartindent
set foldmethod=manual
set foldenable


" Search Settings
set hlsearch
set incsearch
set ignorecase
set smartcase


" Behaviour Settings
set wrap
set lazyredraw
set nu
set rnu
set showmatch
set vb
set wildmenu
set autoread
set encoding=utf-8
set clipboard=unnamed
set tw=79


" Appearance Settings
" colorscheme material
" let g:material_theme_style = 'default'
set colorcolumn=80
highlight colorcolumn ctermbg=7
highlight Folded ctermbg=None
set fillchars=""
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1


" Plugins
call plug#begin()
Plug 'scrooloose/nerdTree'    " File Explorer
Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }    " Completer
Plug 'ctrlpvim/ctrlp.vim'    " Fuzzy file finder
Plug 'jistr/vim-nerdtree-tabs'    " NT tabs
Plug 'bling/vim-airline'    " Powerline
Plug 'Raimondi/delimitMate'    " Matchpairer
call plug#end()


" Plugin Settings
let g:airline_powerline_fonts = 1
let g:airline#extensions#tabline#enabled = 1
" delimitMate
let delimitMate_expand_cr = 1
augroup mydelimitMate
  au!
  au FileType markdown let b:delimitMate_nesting_quotes = ["`"]
  au FileType tex let b:delimitMate_quotes = ""
  au FileType tex let b:delimitMate_matchpairs = "(:),[:],{:},`:'"
  au FileType python let b:delimitMate_nesting_quotes = ['"', "'"]
augroup END
