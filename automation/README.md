## Automação de Login com Selenium (Windows)

### Pré-requisitos
- **Python 3.10+** instalado (verifique com `python --version`)
- **Google Chrome** ou **Microsoft Edge** instalado
- Permissão de rede para o Selenium baixar o WebDriver automaticamente (Selenium Manager)

### Passo a passo (Windows PowerShell)
1. Entre na pasta do projeto:
   ```powershell
   cd C:\programacao\python\automation
   ```
2. Crie e ative um ambiente virtual:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
   Se houver erro de política de execução, rode PowerShell como Administrador:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Instale as dependências:
   ```powershell
   pip install -r requirements.txt
   ```
4. Configure suas variáveis de ambiente copiando o exemplo:
   ```powershell
   copy .env.example .env
   ```
   Edite `.env` e preencha:
   - **URL**: URL inicial da aplicação
   - **BROWSER**: `chrome` ou `edge`
   - **HEADLESS**: `true` ou `false`
   - **DISPLAY_MODE**: `true` para ver passos na tela, ignora `HEADLESS`
   - **STEP_DELAY_MS**: delay em ms entre ações no modo de exibição (ex.: 600)
   - **KEEP_OPEN**: `true` para manter a janela aberta ao final (Chrome usa detach)
   - **STOP_ON_ERROR**: `true` para pausar no erro e esperar `Enter`
   - **WINDOW_WIDTH**, **WINDOW_HEIGHT**: tamanho da janela (ex.: 1366x768)
   - **ATTACH_TO_BROWSER**: `true` para conectar a um navegador já aberto
   - **DEBUGGER_ADDRESS**: endereço do debugger (ex.: `127.0.0.1:9222`)
   - **OPEN_NEW_TAB**: `true` para abrir em nova aba ao anexar
   - **INPUT_ONE_VALUE**, **INPUT_TWO_VALUE**, **OPTION_TEXT**
5. Preencha os XPaths em `src/config.py` na seção `Locators`.
6. Execute a automação:
   ```powershell
   python -m src.main
   ```

### Modo de exibição
- Ative com `DISPLAY_MODE=true`.
- Destaques visuais dos elementos e delays são aplicados.
- Se `KEEP_OPEN=true`, a janela permanece aberta ao final do fluxo (Chrome). Em Edge, a janela pode fechar ao encerrar o processo.
- Se ocorrer erro e `STOP_ON_ERROR=true`, o script aguardará `Enter` antes de fechar.

### Anexar a um navegador já aberto
1. Inicie o Chrome em modo de depuração remota:
   ```powershell
   & "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\\ChromeDebug"
   ```
   Ou Edge:
   ```powershell
   & "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe" --remote-debugging-port=9222 --user-data-dir="C:\\EdgeDebug"
   ```
2. No `.env`:
   ```dotenv
   ATTACH_TO_BROWSER=true
   DEBUGGER_ADDRESS=127.0.0.1:9222
   OPEN_NEW_TAB=true
   DISPLAY_MODE=true
   HEADLESS=false
   ```
3. Execute o script. Ele anexará na janela já aberta e, se configurado, abrirá uma nova aba antes de navegar.

### Dicas para capturar XPaths
- Abra o site, pressione `F12` para abrir DevTools.
- Clique com o botão direito no elemento → Inspecionar → clique com o direito no nó → Copy → Copy XPath.
- Prefira XPaths estáveis (por atributos fixos) a XPaths com índices.

### Problemas comuns
- Se o browser não abrir: garanta que o navegador está instalado e atualizado.
- Se demorar para encontrar elementos: ajuste `IMPLICIT_WAIT`/`EXPLICIT_WAIT` em `src/config.py`.
- Para visualizar o fluxo: `DISPLAY_MODE=true` e ajuste `STEP_DELAY_MS`.
- Para manter a janela aberta ao final: `KEEP_OPEN=true` (melhor suporte no Chrome).
- Para anexar a navegador aberto: inicie com `--remote-debugging-port` e configure `ATTACH_TO_BROWSER=true` no `.env`.

### Estrutura
```
automation/
  requirements.txt
  .env.example
  README.md
  src/
    __init__.py
    config.py
    driver.py
    utils.py
    main.py
    pages/
      __init__.py
      screen_one.py
      screen_two.py
      screen_three.py
```
