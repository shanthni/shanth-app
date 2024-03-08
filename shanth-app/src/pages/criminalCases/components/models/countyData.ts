
export interface data {
    data: cases[],
    name: string
}

export interface cases {
    defendant_key: string,
    id: number,
    proceeding_date: string | null,
    disposition: string | null,
    offense: string | null,
    prison_time: number | null,
    fine: number | null,
    prob_time: number | null  
}
