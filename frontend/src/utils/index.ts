export function calcul_prix_tva_inclu(prix_hors_tva: number): number {
  return prix_hors_tva + prix_hors_tva * 0.2;
}
