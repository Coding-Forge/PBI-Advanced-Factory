# Customer Branding

Branding is controlled by `scripts\delivery-config.js`.

For each customer engagement:

1. Create a folder under `Branding\CustomerName`.
2. Add logo or badge SVG/PNG files.
3. Update `scripts\delivery-config.js` with customer name, workshop name, logo path, badge path, and theme values.
4. Open `index.html` to verify the masthead and accent color.

You can also test an alternate config by opening a page with:

```text
?brandConfig=Branding/CustomerName/delivery-config.js
```

Theme keys:

- `accent`
- `accentHover`
- `accentSoft`
- `accentForeground`
- `link`

Keep all lab HTML styling on the Clawpilot variables. Branding should only override the allowed variables through configuration.