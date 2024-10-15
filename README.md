# MinForening Web

Dette repository indeholder MinForenings web interface; i daglige tale MinForening Web, MF Web eller bare Web.

## Basics

Projektet er udviklet med [`create-react-app`](https://github.com/facebook/create-react-app), som håndterer alle build scripts, Webpack-konfigurationer, etc.
For at kører projektet kræves der
 * [en supporteret version af Node.js](https://nodejs.org/en/about/releases/). Det seneste long-term support er altid et godt bud (i skrivende stund 14.17.3)
 * [`yarn`](https://yarnpkg.com) til dependency management

### Dependencies
 * `yarn install` installerer dependencies.
 * Kør `yarn outdated` engang i mellem for at holde øje med opdatering til dependencies; opdater med `yarn upgrade`/`yarn upgrade-interactive`.
   * **OBS:** [`date-fns`](https://github.com/date-fns/date-fns), [`react-redux`](https://github.com/reduxjs/react-redux) og [`react-router-dom`](https://github.com/ReactTraining/react-router) er bevidst bagud i version, da dele af Web bruger gamle funktioner. Der bruges en [forked version](https://github.com/emilbaekdahl/react-datetime) af [`react-datetime`](https://github.com/YouCanBookMe/react-datetime); derfor vil den dukke op under `yarn outdated`, men kan/skal ikke opdateres.

### Development
 * `yarn start` kører en development server på port 3000. Vær opmærksom på, at der bruges HTTPS lokalt. De fleste browsere brokker sig over det, da det giver anledning til brug af self-signed certifikater. Det bør dog være rimelig simpelt at komme omkring. Et par søgninger eller to på internettet er nok tilstrækkeligt.
 * [`eslint`](https://eslint.org) kører gennem `create-react-app`, og development serveren giver derfor besked om eventuelle linting fejl/advarsler.
 * `yarn prettier` kører [`prettier`](https://prettier.io), som laver grim kode til flot (og ikke mindst konsekvent formateret) kode. Brug det.

### Test
 * `yarn test` kører alle tests.
 * Der er få tests i projektet, som blev skrevet i begyndelsen. Det er ikke en vane, der er blevet holdt ved lige. Lad være med at lægge for meget i det.

### Build
 * `yarn build` bygger projektet til en række statiske filer i `build/`-mappen, som derefter kan sendes i produktion.

### Deployment
 * MinForening har et team på [Heroku](https://heroku.com) med en enkelt server af typen [Hobby](https://www.heroku.com/pricing#containers), der bruges som produktionsmiljø.

## Internationalisering
 * Vi bruger [`react-i18next`](https://react.i18next.com) til at håndtere flere sprog på Web.
 * Hvert sprog har sin egen JSON-fil i `src/locales`, som mapper alle danske tekster til en på det relevante sprog tilsvarende tekst.
 * Når der tilføjes ny tekst, skal det naturligvis oversættes fra danske til engelsk og tysk. Det gør vi på følgende måde.
   * Den nye tekst tilføjes til den danske oversættelsesfil (`src/locales/da/translation.json`)
   * Scriptet `generate_translation_template.py` køres (`python generate_translation_template.py`) og genererer en CSV-fil, som sendes til Peter.
   * Peter sender en ny CSV-fil retur med de manlgende oversættelser.
   * Scriptet `import_translations.py` køres (`python import_translations.py path/to/file.csv`) med den nye CSV-fil som input.

## Opsætning for at starte projektet

Grundet vores react js version er af ældre dato, så skal vi køre følgende ved install "npm i --legacy-peer-dep" og ved "npm start" skal vi indimellem skrive " $env:NODE_OPTIONS = "--openssl-legacy-provider" " i terminalen før vi kan benytte npm start.

Følgende skal være i index.html til udvikling for <head>
    <meta name="readyMinOrganisation" content="false">
    <meta name="useMinOrganisation" content="false">
    <meta name="tenantApi" content="https://tenant-api.softnotik.dk/api">
    <meta name="growthBookUrl" content="">
    <meta name="apiMyOrgUrl" content="https://api-dev.minforening.dk/api">

## Arkitektur
Første nogle ord om de primære dependencies, som projektet bygger på.
 * Projektets hovedkomponent er [`react`](https://reactjs.org).
 * [`redux`](https://redux.js.org) bruges til state management (i naturlig kombinatin med [`react-redux`](https://react-redux.js.org)).
 * Side-effects (primært API-kald i dette projekt) håndteres af [`redux-saga`](https://redux-saga.js.org).
 * Tilgangen til styling er CSS-in-JS. Det gøres med udgangspunkt i [`styled-components`](https://styled-components.com) og [`styled-system`](https://styled-system.com). Der er sjældent behov for at lave nye komponenter med styling, da der allerede er mange klar til brug i `src/components/`.
 * Håndtering af formulare (f.eks. til oprettelse af aktiviteter og betalinger) gøres med [`formik`](https://jaredpalmer.com/formik/). Validering klares med [`yup`](https://github.com/jquense/yup), som [`formik` integrer godt med](https://jaredpalmer.com/formik/docs/guides/validation#validationschema).

Og så noget om strukturen i projektet.

 * `src/` indeholder en række undermapper, der cirka svarer til de forskellige dele af system. F.eks. `members/`, `activities/` og `payments/`. Hver af disse har blandt andet sin egen [`redux` reducer](https://redux.js.org/basics/reducers/), [actions](https://redux.js.org/basics/actions#actions), en samling [selectors](https://redux.js.org/introduction/learning-resources#selectors) og selvfølgelig nogle React-komponenter.
 * Web var oprindeligt designet som et værktøj for administratorer og gruppeledere, mens smartphone appen var tiltænkt "almindelige" medlemmer. Det er siden blevet besluttet, at Web også skal kunne bruges af sidstnævnte. I praksis betyder det, at der er lavet et nyt "system i system". Mappen `memberPerspective` indeholder på en måde sin egen lille web app, der er mere eller mindre isoleret fra de andre dele af Web (her er nogle få undtagelser som f.eks. håndtering af login).

## Kode Standard
Efter Softnotiks overtagelse af projektet skrives alt i koden på engelsk frem for dansk.