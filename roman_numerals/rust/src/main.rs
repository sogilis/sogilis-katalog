#[cfg(test)]
#[path = "./romanian_test.rs"]
mod romanian_test;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        return;
    }
    let input = args.get(1).unwrap();

    let count = romanian_count(input);
    if count > 0 {
        println!("\n{}", count);
    }
}

fn romanian_count(input: &String) -> i32 {
    input.chars().count() as i32
}


