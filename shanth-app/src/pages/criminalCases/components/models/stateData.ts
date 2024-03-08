import { Feature } from "geojson";

export interface data {
  census_data: census[];
  offense_data: offense[];
  geo_data: geo;
  id: number;
  stats: stats[];
  state: string;
}

export interface census {
  case_ratio: number | null;
  county_name: string | null;
  income: number | null;
  population: number | null;
}

export interface offense {
  off_count: number;
  offense: string;
}

export interface geo {
  coordinates: [x: number, y: number];
  features: Feature;
}

export interface stats {
  case_count: number;
  fine: number;
  prison: number;
  probation: number;
}
