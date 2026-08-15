(() => {
  const defaultBrand = {
    customerName: "Customer",
    workshopName: "Power BI Advanced Factory",
    titleSuffix: "",
    logoPath: "",
    badgePath: "",
    theme: {},
    icons: {}
  };
  const cssVarNames = {
    accent: "--cp-accent",
    accentHover: "--cp-accent-hover",
    accentSoft: "--cp-accent-soft",
    accentForeground: "--cp-accent-fg",
    link: "--cp-link"
  };
  const style = document.createElement("style");
  style.textContent = `
    .delivery-brand { display: flex; align-items: center; gap: 12px; min-height: 66px; padding: 12px 0; border-bottom: 1px solid var(--cp-border); }
    .delivery-brand__mark { width: 40px; height: 40px; display: grid; flex: 0 0 40px; place-items: center; overflow: hidden; background: var(--cp-accent); color: var(--cp-accent-fg); border-radius: 0.625rem; font-weight: 800; }
    .delivery-brand__mark img { width: 100%; height: 100%; padding: 6px; object-fit: contain; background: var(--cp-surface); }
    .delivery-brand__badge { display: block; width: min(100%, 430px); max-height: 74px; object-fit: contain; object-position: left center; }
    .delivery-brand__name, .delivery-brand__workshop { display: block; letter-spacing: 0; }
    .delivery-brand__name { color: var(--cp-text); font-size: 1rem; font-weight: 800; }
    .delivery-brand__workshop { color: var(--cp-text-muted); font-size: 0.78rem; }
  `;
  document.head.appendChild(style);

  function getConfigPath() {
    const script = document.currentScript || [...document.scripts].find((item) => item.src.endsWith("/delivery-brand.js"));
    const queryConfig = new URLSearchParams(window.location.search).get("brandConfig");
    return queryConfig || script?.dataset.config || "scripts/delivery-config.js";
  }
  function mergeBrandConfig(config) {
    return { ...defaultBrand, ...config, theme: { ...defaultBrand.theme, ...(config?.theme || {}) }, icons: { ...defaultBrand.icons, ...(config?.icons || {}) } };
  }
  function applyTheme(theme) {
    Object.entries(cssVarNames).forEach(([key, cssVar]) => {
      if (theme[key]) document.documentElement.style.setProperty(cssVar, theme[key]);
    });
  }
  function createMark(brand) {
    const mark = document.createElement("span");
    mark.className = "delivery-brand__mark";
    if (brand.logoPath) {
      const image = document.createElement("img");
      image.src = brand.logoPath;
      image.alt = "";
      mark.appendChild(image);
    } else {
      mark.textContent = (brand.customerName || "C").slice(0, 1).toUpperCase();
    }
    return mark;
  }
  function createTextBrand(brand) {
    const text = document.createElement("span");
    const customer = document.createElement("strong");
    customer.className = "delivery-brand__name";
    customer.textContent = brand.customerName;
    const workshop = document.createElement("span");
    workshop.className = "delivery-brand__workshop";
    workshop.textContent = brand.workshopName;
    text.append(customer, workshop);
    return text;
  }
  function createBadge(brand) {
    const badge = document.createElement("img");
    badge.className = "delivery-brand__badge";
    badge.src = brand.badgePath;
    badge.alt = `${brand.customerName} ${brand.workshopName}`;
    badge.onerror = () => badge.replaceWith(createMark(brand), createTextBrand(brand));
    return badge;
  }
  function renderBrand(brand) {
    applyTheme(brand.theme);
    const shell = document.querySelector(".shell");
    if (!shell || shell.querySelector(".delivery-brand")) return;
    const masthead = document.createElement("div");
    masthead.className = "delivery-brand";
    masthead.setAttribute("aria-label", `${brand.customerName} ${brand.workshopName}`);
    if (brand.badgePath) masthead.appendChild(createBadge(brand));
    else masthead.append(createMark(brand), createTextBrand(brand));
    shell.prepend(masthead);
    const suffix = brand.titleSuffix || brand.customerName;
    if (suffix && !document.title.endsWith(` - ${suffix}`)) document.title = `${document.title} - ${suffix}`;
  }
  function loadConfig() {
    return new Promise((resolve) => {
      if (window.deliveryBrandConfig) return resolve(window.deliveryBrandConfig);
      const script = document.createElement("script");
      script.src = getConfigPath();
      script.defer = true;
      script.onload = () => resolve(window.deliveryBrandConfig || {});
      script.onerror = () => resolve({});
      document.head.appendChild(script);
    });
  }
  const ready = (callback) => document.readyState === "loading" ? document.addEventListener("DOMContentLoaded", callback, { once: true }) : callback();
  loadConfig().then((config) => ready(() => renderBrand(mergeBrandConfig(config))));
})();